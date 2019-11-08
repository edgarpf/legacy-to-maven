import os
import ntpath
import platform
from os import listdir
from os.path import isfile, join
from pathlib import Path

url="" #fill
groupId="" #fill
repositoryId="" #fill
version="" #fill
scriptName=os.path.basename(__file__)
isWindows= platform.system() == 'windows'
uploadFileName= "upload.bat" if isWindows else "upload.sh"
dependenciesFileName="dependencies.xml"

myPath = os.path.dirname(os.path.realpath(__file__)) + "\\"
onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]

script = ""
dependencies=""

def createFile(text, fileName):    
    file = open(myPath + fileName,"w+")
    file.write(text)
    file.close()

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

for filePath in Path(os.path.dirname(os.path.realpath(__file__))).rglob('*.jar'):
    fileName = path_leaf(str(filePath))[:-4]
    if(isWindows):
        script = script + "call "
    script = script + "mvn deploy:deploy-file -DrepositoryId="+ repositoryId +" -Durl=" + url +" -DgroupId="+ groupId +" -Dversion="+ version +" -DgeneratePom=true -Dpackaging=jar "+ "-Dfile=" + str(filePath) + " -DartifactId=" + fileName + "\n\n"
    dependencies = dependencies +  "<dependency>\n\t<groupId>" + groupId + "</groupId>" + "\n\t<artifactId>" + fileName + "</artifactId>" + "\n\t<version>" + version + "</version>\n</dependency>\n"

createFile(script if isWindows else "#!/bin/bash \n\n" + script, uploadFileName)
createFile(dependencies, dependenciesFileName)
