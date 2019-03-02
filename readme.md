**Requirements**
=============

1. python
2. Python packages:
	- tweepy
	- request
	- facebook-sdk
	- oauth2


**Usage**
======

$ make

if Make is not installed
------------------------
$ python main.py


**Notes**
=====

1. Make sure "JSON" folder exist
2. This code implements projects: <br/>
   [LINKCUBE: A Tool for Anomaly Detection in Social Network using GBAD](https://rpaudel42.github.io/assets/LinkCube_Report.pdf)

**Description**
LinkCube is command-line based tool written in Python.
LinkCube processes the data between a social network that resides on the internet and GBAD.
LinkCube is composed of two layers: the first layer is the data extraction layer, and the second layer is the data processing layer.
The data extraction layer has three modules that invoke data requests to each of the three social networks (Twitter, Facebook and LinkedIn).
Each module receives data in the JSON format and forwards it to their respective parser in the data processing layer.
The data processing layer gathers the data, processes the data, and converts the data into a graph.
The data processing layer has an individual parser for each of the modules in the data extraction layer.
The output from the data processing layer is in the form of a graph.
This output graph can then be run in GBAD to discover an anomaly.



