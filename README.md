# legacy-to-maven
A Python script that helps you convert a Java legacy project to a Maven project

## Use Case

You have a Java legacy project with many local jars. You want to convert it to a Maven project. 

## Pre-requisites

1 - Install Maven and Python on your local machine.

2 - You need to have Nexus server. It will be your Maven repository. 

3 - [Configure Maven and Nexus](https://blog.sonatype.com/using-nexus-3-as-your-repository-part-1-maven-artifacts)

## What does the script do?

It generates two files. 

One of them will be a script to upload all the jars in the project to Nexus. The script detects your operational system and generates a .bat if you are using windows or a .sh file if not.

The other one will be a .xml file with Maven dependecies. You can put its content in a pom.xml file. 

## How do I use the script?

1 - Put the script in the root of your project. 

2 - Open it and fill the required data. 

3 - Run it:

```
py legacy_to_maven.py
```

4 - Run the script generated. It will upload all the jars in the project to your Nexus server.
