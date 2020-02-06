#!/usr/bin/env python

import json
import os
import shutil
import re
import requests
import zipfile, io
from jinja2 import Environment, FileSystemLoader

templates = FileSystemLoader('./templates')
env = Environment(loader=templates)

with open('configuration.json') as json_data_file:
    configuration = json.load(json_data_file)

proxyDict = { 
    #"http"  : "<proxy>", 
    #"https" : "<proxy>"
}

def getDigit(val):
    if val.isdigit(): return int(val)
    else: return (ord(val) - 87) 

release_documents = {}

baseGitURL = "https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/"

for doc in configuration:
    directoryName = doc["id"] + " - " + doc["name"]
    print(directoryName)

    m = re.search('TS (\d+)\.(\d+)', doc["id"])
    serie = m.group(1)
    docId = m.group(2)

    m = re.search('(\d)(\d)(\d)', docId)
    docgroup = m.group(1)

    lastRelease = 0
    releaseDoc = None

    for relase in doc["releases"]:

        directory = "../documentation/" + directoryName + "/Rel-" + str(relase)
        if os.path.exists(directory):
            shutil.rmtree(directory)

        os.makedirs(directory)

        getSeriesURL = "https://www.etsi.org/deliver/etsi_ts/1" +str(serie) + str(docgroup) + "00_1" +str(serie) + str(docgroup) + "99/1" +str(serie) + str(docId) +"/"
        r = requests.get(getSeriesURL, proxies=proxyDict)
        idArray = re.findall(r"etsi_ts\/1" +str(serie) + str(docgroup) + "00_1" +str(serie) + str(docgroup) + "99\/1" +str(serie) + str(docId) + "\/"+ str(relase).zfill(2) + "\.([\w+|\.]+)\/", r.text)
        
        if(len(idArray) == 0): continue
        idArray.sort()
        id = idArray[len(idArray)-1]

        getSeriesURL = "https://www.etsi.org/deliver/etsi_ts/1" +str(serie) + str(docgroup) + "00_1" +str(serie) + str(docgroup) + "99/1" +str(serie) + str(docId) +"/" + str(relase).zfill(2) + "." + str(id) + "/"
        r = requests.get(getSeriesURL, proxies=proxyDict)

        pdfFile = re.findall(r"\/(\w+).pdf", r.text)
        if(len(pdfFile) == 0): continue
        pdf = pdfFile[0]

        getSeriesURL = getSeriesURL + "/" + str(pdf) + ".pdf"
        r = requests.get(getSeriesURL, proxies=proxyDict)

        with open(directory + '/' + str(pdf) + '.pdf', 'wb') as f:
            f.write(r.content)
        
        if relase > lastRelease: 
            lastRelease = relase
            releaseDoc = directoryName + "/Rel-" + str(relase) + '/' + str(pdf) + '.pdf'

    if lastRelease != 0:
        release_documents[doc["id"]] = baseGitURL + releaseDoc.replace(" ", "%20")

readme_template = env.get_template('README.j2')
output = readme_template.render(release_documents=release_documents)

f = open("../README.md", "w")
f.write(output)
f.close

shutil.rmtree("../apis")
os.makedirs("../apis")

getOpenAPI = "http://www.3gpp.org/ftp/Specs/latest/Rel-15/OpenAPI/"
r = requests.get(getOpenAPI, proxies=proxyDict)
urlAPI = re.findall(r"OpenAPI\/(\w+).yaml", r.text)
for url in urlAPI:
    getOpenAPIFile = getOpenAPI + url + ".yaml"
    r = requests.get(getOpenAPIFile, proxies=proxyDict)
    open("../apis/" + url + ".yaml", 'wb').write(r.content)

getOpenAPI = "http://www.3gpp.org/ftp/Specs/latest/Rel-16/OpenAPI/"
r = requests.get(getOpenAPI, proxies=proxyDict)
urlAPI = re.findall(r"OpenAPI\/(\w+).yaml", r.text)
for url in urlAPI:
    getOpenAPIFile = getOpenAPI + url + ".yaml"
    r = requests.get(getOpenAPIFile, proxies=proxyDict)
    open("../apis/" + url + ".yaml", 'wb').write(r.content)