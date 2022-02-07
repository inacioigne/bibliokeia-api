from xml.dom import minidom
from src.db.models import Item
from src.db.init_db import session
import xml.etree.ElementTree as et
from copy import deepcopy
import json

def create_marcxml(model_item):
    doc = minidom.Document()
    record = doc.createElement('record')
    #100
    datafield_100 = doc.createElement('datafield')
    datafield_100.setAttribute('tag', '100')
    datafield_100.setAttribute('ind1', '1')
    datafield_100.setAttribute('ind2', ' ')
    subfield_100_a = doc.createElement('subfield')
    subfield_100_a.setAttribute('code', 'a')
    text_100_a = doc.createTextNode(model_item.marc_100_a)
    subfield_100_a.appendChild(text_100_a)
    datafield_100.appendChild(subfield_100_a)
    subfield_100_d = doc.createElement('subfield')
    subfield_100_d.setAttribute('code', 'd')
    text_100_d = doc.createTextNode('1952-')
    subfield_100_d.appendChild(text_100_d)
    datafield_100.appendChild(subfield_100_d)
    record.appendChild(datafield_100)
    #245
    datafield_245 = doc.createElement('datafield')
    datafield_245.setAttribute('tag', '245')
    datafield_245.setAttribute('ind1', '1')
    datafield_245.setAttribute('ind2', '0')
    subfield_245_a = doc.createElement('subfield')
    subfield_245_a.setAttribute('code', 'a')
    text_245_a = doc.createTextNode(model_item.marc_245_a)
    subfield_245_a.appendChild(text_245_a)
    datafield_245.appendChild(subfield_245_a)
    subfield_245_c = doc.createElement('subfield')
    subfield_245_c.setAttribute('code', 'c')
    text_245_c = doc.createTextNode('Milton Hatoum ; translated by John Gledson.')
    subfield_245_c.appendChild(text_245_c)
    datafield_245.appendChild(subfield_245_c)
    record.appendChild(datafield_245)
    #260
    datafield_260 = doc.createElement('datafield')
    datafield_260.setAttribute('tag', '260')
    datafield_260.setAttribute('ind1', ' ')
    datafield_260.setAttribute('ind2', ' ')
    subfield_260_a = doc.createElement('subfield')
    subfield_260_a.setAttribute('code', 'a')
    text_260_a = doc.createTextNode(model_item.marc_260_a)
    subfield_260_a.appendChild(text_260_a)
    datafield_260.appendChild(subfield_260_a)
    subfield_260_b = doc.createElement('subfield')
    subfield_260_b.setAttribute('code', 'b')
    text_260_b = doc.createTextNode(model_item.marc_260_b)
    subfield_260_b.appendChild(text_260_b)
    datafield_260.appendChild(subfield_260_b)
    subfield_260_c = doc.createElement('subfield')
    subfield_260_c.setAttribute('code', 'c')
    text_260_c = doc.createTextNode(model_item.marc_260_c)
    subfield_260_c.appendChild(text_260_c)
    datafield_260.appendChild(subfield_260_c)
    record.appendChild(datafield_260)
    doc.appendChild(record)

    return doc.toprettyxml(encoding='utf-8')

def create_marcjson(item_request):

    print(item_request.leader)


def create_item(item_request):
    marcjson = item_request.json()
    marcdict = json.loads(marcjson) 
    print(marcdict)
    
    item = Item(
            title = marcdict.get('datafield').get('tag_245').get('a'),
            marc = marcdict
            )
    session.add(item)
    session.commit()
    
    return {'msg': 'Item created successefully'}

def edit_item(item_id, item_edit):
    item = session.query(Item).filter_by(id = item_id).first()
    marc = deepcopy(item.marc)
    for k in item_edit.datafield.keys():
        for subfield, v in item_edit.datafield.get(k).items():
            if marc.get('datafield').get(k):
                marc.get('datafield').get(k)[subfield] = v
                print(marc.get('datafield').get(k)[subfield])
            else:
                marc.get('datafield')[k] = {subfield: v}
    datafield = {
        k: v for k, v in sorted(marc.get('datafield').items())
    }
    marc['datafield'] = datafield
    item.marc = marc
    #item.title = item_edit.datafield.get('tag_245').get('a')
    session.commit()

    return {'msg': 'Item updated successefully'}