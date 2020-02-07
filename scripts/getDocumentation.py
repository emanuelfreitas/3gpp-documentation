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

api_urls =  {}
release_documents = {}

def getAPIURL(api):
    return "https://editor.swagger.io/?url=https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/" + api +".yaml"

def getDigit(val):
    if val.isdigit(): return int(val)
    else: return (ord(val) - 87) 

def getAPI(getOpenAPI, regrularExpression):
    r = requests.get(getOpenAPI, proxies=proxyDict)
    urlAPI = re.findall(regrularExpression, r.text)
    for url in urlAPI:
        getOpenAPIFile = getOpenAPI + url + ".yaml"
        if os.path.exists("../apis/" + url + ".yaml"): continue
        r = requests.get(getOpenAPIFile, proxies=proxyDict)
        open("../apis/" + url + ".yaml", 'wb').write(r.content)
        api_urls[url] = getAPIURL(url)

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
        if not os.path.exists(directory):
            os.makedirs(directory)

        filesInDir = os.listdir(directory)

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

        if str(pdf)+".pdf" in filesInDir: 
            filesInDir.remove(str(pdf)+".pdf")
        else:
            getSeriesURL = getSeriesURL + "/" + str(pdf) + ".pdf"
            r = requests.get(getSeriesURL, proxies=proxyDict)

            with open(directory + '/' + str(pdf) + '.pdf', 'wb') as f:
                f.write(r.content)

        for f in filesInDir:
            print("GOING TO REMOVE: " + directory + "/" + f)
            os.remove(directory + "/" + f)
        
        if relase > lastRelease: 
                lastRelease = relase
                releaseDoc = directoryName + "/Rel-" + str(relase) + '/' + str(pdf) + '.pdf'

    if lastRelease != 0:
        release_documents[doc["id"]] = baseGitURL + releaseDoc.replace(" ", "%20")

shutil.rmtree("../apis")
os.makedirs("../apis")

getAPI("http://www.3gpp.org/ftp/Specs/latest/Rel-16/OpenAPI/", r"OpenAPI\/(\w+).yaml")
getAPI("https://www.3gpp.org/ftp/Specs/archive/OpenAPI/Rel-16/", r"Rel-16\/(\w+).yaml")
getAPI("http://www.3gpp.org/ftp/Specs/latest/Rel-15/OpenAPI/", r"OpenAPI\/(\w+).yaml")
getAPI("https://www.3gpp.org/ftp/Specs/archive/OpenAPI/Rel-15/", r"Rel-15\/(\w+).yaml")

readme_template = env.get_template('README.j2')
output = readme_template.render(release_documents=release_documents,api_urls=api_urls)

f = open("../README.md", "w")
f.write(output)
f.close