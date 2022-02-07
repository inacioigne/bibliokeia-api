import json
import xml.etree.ElementTree as et

def xml_to_json(marcxml):
  root = et.fromstring(marcxml)
  marcjson = {'leader': root[0].text }
  controfield = dict()
  datafield = dict()
  for child in root[1:]:
    tag = child.tag.split('}')[1]
    if tag == 'controlfield':
      controfield['tag_'+child.attrib['tag']] = child.text
    elif tag == 'datafield':
      subfields = {
        'ind1': child.attrib['ind1'],
        'ind2': child.attrib['ind2']
      }
      for subfield in child:
        subfields[subfield.attrib['code']] = subfield.text
      datafield['tag_'+child.attrib['tag']] = subfields
  marcjson['controfield'] = controfield
  marcjson['datafield'] = datafield

  return marcjson