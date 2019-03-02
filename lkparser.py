'''
 * This module will use Linked JSON File and convert the JSON data into a graph
 * This graph file is used by GBAD to find the anomaly detection later on
 * Python Version 2.7
 *
 *
 * @Layer      		DataProcessing Layer
 * @Module     		LinkedIn Parser Module
 * @Author     		Ramesh Paudel <rpaudel42@students.tntech.edu>
 * @LastModifiedDate 	April 08 2014
'''

import json,re,sys, getopt

class LinkedInParser():

	def __init__(self):
		print "\n\n ---- Starting Facebook Parser ---"

	def  linkedin_parser(argv):
		source = '';
		dest = '';

		try:
			opts,args = getopt.getopt(argv,"hs:g:",["source=","graph="])
		except getopt.GetoptError:
			print 'lkparser.py -s <SOURCE FILE> -g <GRAPH FILE>'
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				print 'lkparser.py -s <SOURCE FILE> -g <GRAPH FILE>'
				sys.exit();
			elif opt in("-s", "--source"):
				source = arg;
			elif opt in("-g", "--graph"):
				dest = arg;

		fw = open(dest,"a");
		data = json.loads(open(source).read())
		j=1
		for line in data["values"]:
			fw.write("XP # "+str(j)+"\n")
			j = j+1
			i=0
			if (line["firstName"] is not None ):
				i = i+1
				user = i
				fw.write("v "+ str(i) +" \"user\"\n")
				text=i
			if (line["location"] is not None ):
				i = i+1
				fw.write("v "+ str(i) + " \""+line["location"]["country"]["code"]+"\"\n")
				fw.write("d "+ str(i-1) +" " + str(i) +" \"loc\"\n")
				if(line["positions"]["_total"]>0):
					for pos in (line["positions"]["values"]):
						if(pos["isCurrent"]):
							i = i+1
							fw.write("v "+ str(i) + " \"job\"\n")
							fw.write("d "+ str(user) +" " + str(i) +" \"work_for\"\n")