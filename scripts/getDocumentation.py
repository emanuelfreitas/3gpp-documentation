#!/usr/bin/env python

import json
import os, glob
import shutil
import re
import urllib.request
import zipfile, io
from jinja2 import Environment, FileSystemLoader

templates = FileSystemLoader('./templates')
env = Environment(loader=templates)

with open('configuration.json') as json_data_file:
    configuration = json.load(json_data_file)

api_urls =  {}
release_documents = {}

def getURLAsJSON(url):
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            encoding = response.info().get_content_charset('utf-8')
            return json.loads(the_page.decode(encoding))
    except Exception as e:
        pass

    return None

def getURLAsString(url):
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            encoding = response.info().get_content_charset('utf-8')
            return str(the_page.decode(encoding))
    except Exception as e:
        pass

    return None

def getURL(url):
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            return response.read()
    except Exception as e:
        print(e)
        pass

    return None

def getAPIURL(api):
    return "https://emanuelfreitas.github.io/3gpp-documentation/apis/html/" + api + ".html"

def getDigit(val):
    if val.isdigit(): return int(val)
    else: return (ord(val) - 87) 

def getAPI(getOpenAPI, regrularExpression):
    print("getAPI:" + str(getOpenAPI))
    urlAPI = re.findall(regrularExpression, str(getURLAsString(getOpenAPI)))
    for url in urlAPI:
        getOpenAPIFile = getOpenAPI + url + ".yaml"
        if os.path.exists("../apis/" + url + ".yaml"): continue        
        
        open("../apis/" + url + ".yaml", 'wb').write(getURLAsString(getOpenAPIFile))

        api_urls[url] = getAPIURL(url)
    print("getAPI Done")


baseGitURL = "https://github.com/emanuelfreitas/3gpp-documentation/raw/master/documentation/"

for ficheiro in glob.glob("../apis/*.yaml"):
    os.remove(ficheiro)

for doc in configuration:
    directoryName = doc["id"] + " - " + doc["name"]
    requiredAPI = doc.get("api", False)
    print(directoryName)

    m = re.search('TS (\d+)\.(\d+)', doc["id"])
    serie = m.group(1)
    docId = m.group(2)

    m = re.search('(\d)(\d)(\d)', docId)
    docgroup = m.group(1)

    lastRelease = 0
    releaseDoc = None
    
    releasesList = list(range(6, 19))
    releasesList.sort(reverse=True)

    for relase in releasesList:
        if lastRelease > 0: continue

        directory = "../documentation/" + directoryName + "/Rel-" + str(relase)
        if not os.path.exists(directory):
            os.makedirs(directory)

        filesInDir = os.listdir(directory)

        getSeriesURL = "https://www.etsi.org/deliver/etsi_ts/1" +str(serie) + str(docgroup) + "00_1" +str(serie) + str(docgroup) + "99/1" +str(serie) + str(docId) +"/"
        idArray = re.findall(r"etsi_ts\/1" +str(serie) + str(docgroup) + "00_1" +str(serie) + str(docgroup) + "99\/1" +str(serie) + str(docId) + "\/"+ str(relase).zfill(2) + "\.([\w+|\.]+)\/", str(getURLAsString(getSeriesURL)))
        
        if(len(idArray) == 0): 
            os.rmdir(directory)
            continue
        idArray.sort(reverse=True)

        id = 0
        pdf = None
        zipF = None
        for index in idArray:
            id = index
            getSeriesURL = "https://www.etsi.org/deliver/etsi_ts/1" +str(serie) + str(docgroup) + "00_1" +str(serie) + str(docgroup) + "99/1" +str(serie) + str(docId) +"/" + str(relase).zfill(2) + "." + str(id) + "/"
            pdfFile = re.search(r"\/(\w+).pdf", getURLAsString(getSeriesURL))
            zipFile = re.search(r"\/(\w+).zip", getURLAsString(getSeriesURL))
            if not pdfFile or (not zipFile and requiredAPI):
                continue
            else:
                pdf = pdfFile.group(1)
                zipF = zipFile.group(1) if zipFile else None
                break

        if not pdf or (not zipF and requiredAPI):
            os.rmdir(directory)
            continue

        if zipF:
            zipURL = getSeriesURL + "/" + str(zipF) + ".zip"
            resp = urllib.request.urlopen(zipURL)
            myzip = zipfile.ZipFile(io.BytesIO(resp.read()))
            for line in myzip.namelist():
                if 'TS' in line and line.endswith('yaml'):
                    ficheiroResultado = re.sub(r'^.*?TS', 'TS', line)

                    temp_path = myzip.extract(line)
                    # Mover e renomear o ficheiro
                    shutil.move(temp_path, '../apis/' + ficheiroResultado)

                    filedata = None
                    with open('../apis/'+str(ficheiroResultado), 'r') as file :
                        filedata = file.read()
                        filedata = filedata.replace('$ref: \'TS', '$ref: \'https://raw.githubusercontent.com/emanuelfreitas/3gpp-documentation/master/apis/TS')
                    with open('../apis/'+str(ficheiroResultado), 'w') as file:
                        file.write(filedata)

                    api_urls[ficheiroResultado.replace(".yaml", "")] = getAPIURL(ficheiroResultado.replace(".yaml", ""))

        if str(pdf)+".pdf" in filesInDir:
            filesInDir.remove(str(pdf)+".pdf")
        else:
            getSeriesURL = getSeriesURL + "/" + str(pdf) + ".pdf"
            the_page = None
            with urllib.request.urlopen(getSeriesURL) as response:
                the_page = response.read()
            with open(directory + '/' + str(pdf) + '.pdf', 'wb') as f:
                f.write(the_page)
        for f in filesInDir:
            print("GOING TO REMOVE: " + directory + "/" + f)
            os.remove(directory + "/" + f)
        
        lastRelease = relase
        releaseDoc = directoryName + "/Rel-" + str(relase) + '/' + str(pdf) + '.pdf'

    if lastRelease != 0:
        release_documents[doc["id"]] = baseGitURL + releaseDoc.replace(" ", "%20")


directory = "../documentation/" + directoryName + "/Rel-" + str(relase)

for raiz, subdirs, _ in os.walk("../documentation/", topdown=False):
    for subdir in subdirs:
        caminho = os.path.join(raiz, subdir)
        if not os.listdir(caminho):
            os.rmdir(caminho)
            
readme_template = env.get_template('README.j2')
output = readme_template.render(release_documents=release_documents,api_urls=api_urls)

f = open("../README.md", "w")
f.write(output)
f.close