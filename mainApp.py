import xml.dom.minidom
import requests
import json
import xmltodict, json


def deleteRequests():
  jsonData = {
    'delete': 'delete'
  }
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive",
    "Content-Type": "application/xml"
  }

  r = requests.post('http://box.rofikit.com/delete.php', headers=headers, json=jsonData)
  print(r.text)


def insertRequests(jsonData):
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive",
    "Content-Type": "application/xml"
  }
  r = requests.post('http://box.rofikit.com/save.php', headers=headers, json=jsonData)
  return (r.text)


def updateRequests(bestellnr,xml,size):
  jsonData = {
    'xml' : xml,
    'size': size,
    'bestellnr': bestellnr
  }
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive",
    "Content-Type": "application/xml"
  }
  r = requests.post('http://box.rofikit.com/update.php', headers=headers, json=jsonData)
  return (r.text)


def getEtikett(xml_doc):
  packages = xml_doc.getElementsByTagName('Etikett')
  xml = 0;
  for package in packages:
    xml        = xml + 1
    bestellnr  = package.getAttribute('bestellnr')
    artsnr     =  package.getElementsByTagName('artsnr')[0].childNodes[0].data
    artikelbez = package.getElementsByTagName('artikelbez')[0].childNodes[0].data
    soko       = package.getElementsByTagName('soko')[0].childNodes[0].data
    plinie     = package.getElementsByTagName('produktlinie')[0].childNodes[0].data
    farbe      = package.getElementsByTagName('farbe')[0].childNodes[0].data
    saison     = package.getElementsByTagName('saison')[0].childNodes[0].data
    kollektion = package.getElementsByTagName('kollektion')[0].childNodes[0].data
    eancode    = package.getElementsByTagName('eancode')[0].childNodes[0].data
    qOfPieces  = package.getElementsByTagName('quantityOfPieces')[0].childNodes[0].data
    sMarking   = package.getElementsByTagName('specialMarking')[0].childNodes[0].data
    sShort     = package.getElementsByTagName('specialMarkingShort')[0].childNodes[0].data
    grossWt    = package.getElementsByTagName('grossWt')[0].childNodes[0].data
    netWt      = package.getElementsByTagName('netWt')[0].childNodes[0].data
    cartonNo   = package.getElementsByTagName('cartonNo')[0].childNodes[0].data
    # print('cartonNo:', cartonNo)
    jsonData = {
      'xml':xml,
      'bestellnr' : bestellnr,
      'artsnr' : artsnr,
      'artikelbez' : artikelbez,
      'soko' : soko,
      'plinie' : plinie,
      'farbe' : farbe,
      'saison' : saison,
      'kollektion' : kollektion,
      'eancode' : eancode,
      'size' : "",
      'qofPieces' : qOfPieces,
      'sMarking' : sMarking,
      'sShort' : sShort,
      'grossWt' : grossWt,
      'netWt' : netWt,
      'cartonNo' : cartonNo,
    }
    ststus = insertRequests(jsonData)
  print(ststus)
  return bestellnr




def updateSize(xml_doc,bestellnr):
  spackages = xml_doc.getElementsByTagName('size')
  xml = 0;
  for spackage in spackages:
    xml  = xml + 1
    size = spackage.getAttribute('sizebez')
    ststus = updateRequests(bestellnr,xml,size)
  print(ststus)

def jsonToxml(url):
  # response = requests.get(url)
  # data = json.loads(response.text)
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
  }
  page = requests.get(url, headers=headers)
  data = json.loads(page.text)

  content: str = '<?xml version="1.0" encoding="utf-8"?>\n<Kartonetiketten xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:de.ttg:intex:kartonetiketten:2014-09-04">\n'

  for item in data:
    xml: str = ('\n'+
    '<Etikett bestellnr="' +item['bestellnr']+ '">\n'
    '<artsnr>' +item['artsnr']+ '</artsnr>\n'
    '<artikelbez>' +item['artikelbez']+ '</artikelbez>\n'
    '<soko>' +item['soko']+ '</soko>\n'
    '<produktlinie>' +item['plinie']+ '</produktlinie>\n'
    '<farbe>' +item['farbe']+ '</farbe>\n'
    '<saison>' +item['saison']+ '</saison>\n'
    '<kollektion>' +item['kollektion']+ '</kollektion>\n'
    '<eancode>' +item['eancode']+ '</eancode>\n'
    '<size sizebez="' +item['size']+ '" />\n'
    '<quantityOfPieces>' + str(item['qofPieces']) + '</quantityOfPieces>\n'
    '<specialMarking>' +item['sMarking']+ '</specialMarking>\n'
    '<specialMarkingShort>' +item['sShort']+ '</specialMarkingShort>\n'
    '<grossWt>' +item['bestellnr']+ '</grossWt>\n'
    '<netWt>' +item['bestellnr']+ '</netWt>\n'
    '<cartonNo>' + str(item['cartonNo']) + '</cartonNo>\n'
    '</Etikett>\n'
    )
    content = content + xml

  content = content + '\n</Kartonetiketten>'
  with open('datafile.xml', 'w') as file:
    file.write(content)



def main():
  deleteRequests()
  xml_doc   = xml.dom.minidom.parse('my.xml')
  bestellnr = getEtikett(xml_doc)
  edit      = updateSize(xml_doc,bestellnr)
  jsonToxml('http://box.rofikit.com/box.php')



if __name__ == "__main__":
  main()


