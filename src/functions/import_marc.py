import httpx
import xml.etree.ElementTree as et
from src.db.init_db import session
from src.db.models import Item, Authority, Subject
from src.functions.marcxml_to_json import xml_to_json

def import_marc_item(request_item):
    if request_item.server == 'LOC':
        baseUrl = request_item.url
        url = baseUrl+'/marcxml'
        r = httpx.get(url)
        marcxml = r.content
        marcjson = xml_to_json(marcxml)
        item = Item(
            title = marcjson.get('datafield').get('tag_245').get('a'),
            marc = marcjson
        )
        session.add(item)
        session.commit()
        return {'msg': 'Item created successefully',
                'itemId': item.id}
    else:
        return {'msg': 'Server not avaliable'}


def import_marc_authority(request_authority):
    baseUrl = request_authority.url.replace('http', 'https')
    format = request_authority.format.lower()
    if format == 'marcxml':
        url = baseUrl+'.marcxml.xml'
        r = httpx.get(url)
        marc_record = r.content
        root = et.fromstring(marc_record)
        author = root.find(".//*[@tag='100']/*/[@code='a']").text
        authority = Authority(
            name = author,
            marc_record = marc_record
        )
        session.add(authority)
        session.commit()

        return {'msg': 'Item created successefully',
                'author': author}
    else:
        return {'msg': 'Fomart Invalid'}

def import_marc_subjects(request_subjects):
    baseUrl = request_subjects.url.replace('http', 'https')
    format = request_subjects.format.lower()
    if format == 'marcxml':
        url = baseUrl+'.marcxml.xml'
        r = httpx.get(url)
        marc_record = r.content
        root = et.fromstring(marc_record)
        name = root.find(".//*[@tag='150']/*/[@code='a']").text
        subject = Subject(
            name = name,
            marc_record = marc_record
        )
        session.add(subject)
        session.commit()

        return {'msg': 'Item created successefully',
                'subject': name}
    else:
        return {'msg': 'Fomart Invalid'}
        


