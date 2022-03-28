marc = {
  "leader": "    nam#a22     4a#4500",
  "controlfield": [
    {
      "003": "BR-MnINPA",
      "005": "20220324184833.0",
      "008": "220324s||||bl #####000#0#por##"
    }
  ],
  "datafield": [
    {
      "100": {
        "Ind2": "#",
        "a": "Oliveira, Inácio",
        "d": "1959-"
      }
    },
    {
      "245": {
        "a": "A amazônia liquída",
        "b": "molhada",
        "c": "Inácio Oliveira"
      }
    },
    {
      "250": {
        "Ind1": "#",
        "Ind2": "#"
      }
    },
    {
      "260": {
        "Ind2": "#"
      }
    },
    {
      "300": {
        "Ind1": "#",
        "Ind2": "#"
      }
    },
    {
      "520": {
        "Ind2": "#"
      }
    },
    {
      "650": {
        "a": "Tambaqui"
      }
    },
    {
      "040": [
        {
          "a": "BR-MnINPA"
        },
        {
          "b": "por"
        }
      ]
    },
    {
      "020": {
        "Ind1": "#",
        "Ind2": "#"
      }
    },
    {
      "650": {
        "a": "Sulamba"
      }
    }
  ]
}

for field in marc["datafield"]:
  if '245' in field.keys():
    print(field['245'].get('a'))

def getTitle(marc):
  for field in marc["datafield"]:
    if '245' in field.keys():
      return field['245'].get('a')
      
