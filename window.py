import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import xml.dom.minidom
import requests
import json
import xmltodict, json

root = Tk()
root.title("Label Generator")
root.geometry("450x400")
ttk.Label(root, text="Add your xml file : ").grid(row=0, column=0, padx=20, pady=20)
open_file = ttk.Button(root, text="Open files")
open_file.grid(row=0, column=1, columnspan=2, padx=20, pady=20)
ttk.Label(root, text="File path : ").grid(row=1, column=0, padx=20, pady=20)
box_red_path = ttk.Label(root, text="")
box_red_path.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
stare_scripte = ttk.Button(root, text="Start")
stare_scripte.grid(row=3, column=1, columnspan=2, padx=20, pady=20)
ttk.Label(root, text="Massage : ",state=DISABLED).grid(row=5, column=0, padx=20, pady=20)
box_massage = ttk.Label(root, text="")
box_massage.grid(row=5, column=1, columnspan=2, padx=20, pady=20)
box_massage.config(state=DISABLED)

def upload_excel():
    filename = filedialog.askopenfilename(
        title="Select a File",
        filetype=(("Excel", "*.xml"), ("Excel", "*.xml"))
    )
    box_red_path.configure(text=filename)
    print("Thanks for xml file")
open_file.config(command=upload_excel)


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
  response = requests.post('http://box.rofikit.com/delete.php', headers=headers, json=jsonData)
  data = json.loads(response.text)
  for item in data:
    print (item['sms'])


def insertRequests(jsonData):
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive",
    "Content-Type": "application/xml"
  }
  response = requests.post('http://box.rofikit.com/save.php', headers=headers, json=jsonData)
  data = json.loads(response.text)
  for item in data:
    return (item['sms'])


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
  response = requests.post('http://box.rofikit.com/update.php', headers=headers, json=jsonData)
  data = json.loads(response.text)
  for item in data:
    return (item['sms'])


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



def start_app():
    url = box_red_path.cget("text")
    deleteRequests()
    xml_doc = xml.dom.minidom.parse(url)
    bestellnr = getEtikett(xml_doc)
    updateSize(xml_doc, bestellnr)
    jsonToxml('http://box.rofikit.com/box.php')
    box_massage.config(text="The process is completed")


stare_scripte.config(command=start_app)
root.mainloop()
