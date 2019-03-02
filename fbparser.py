'''
 * This module will use facebook JSON File and convert the JSON data into a graph
 * This graph file is used by GBAD to find the anomaly detection later on
 * Python Version 2.7
 *
 *
 * @Layer      		DataProcessing Layer
 * @Module     		Facebook Parser Module
 * @Author     		Ramesh Paudel <rpaudel42@students.tntech.edu>
 * @LastModifiedDate 	April 08 2014
'''


import json,re,sys, getopt

class FacebookParser():

	def __init__(self):
		print "\n\n ---- Starting Facebook Parser ---"

	def  facebook_parser(argv):
		source = '';
		dest = '';
		try:
			opts,args = getopt.getopt(argv,"hs:g:",["source=","graph="])
		except getopt.GetoptError:
			print 'fbparser.py -s <SOURCE FILE> -g <GRAPH FILE>'
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				print 'fbparser.py -s <SOURCE FILE> -g <GRAPH FILE>'
				sys.exit();
			elif opt in("-s", "--source"):
				source = arg;
			elif opt in("-g", "--graph"):
				dest = arg;

		fw = open(dest,"a");
		with open(source) as fb_file:
			fb_data = json.load(fb_file)

			nodeCount = 0
			for fields in fb_data['data']:
				for key, value in fields.iteritems():
					nodeCount = nodeCount + 1
					#node[nodeCount]=
					#print key, 'is:', value


			j=1
			for line in fb_data["data"]:

				fw.write("XP # "+str(j)+"\n")
				j = j+1
				i=0

				if (line["name"] is not None ):
					i = i+1
					user = i
					fw.write("v "+ str(i) +" \"user\"\n")
					text=i
				if (line["locale"] is not None ):
					i = i+1
					fw.write("v "+ str(i) + "\""+line["locale"]+"\"\n")
					fw.write("d "+ str(user) +" " + str(i) +" \"lang\"\n")
				if (line["can_post"] is not None ):
					i = i+1
					fw.write("v "+ str(i) + "\"can_post\"\n")
					fw.write("d "+ str(user) +" " + str(i) +" \""+str(line["can_post"])+"\"\n")
				if (line["can_message"] is not None ):
					i = i+1
					fw.write("v "+ str(i) + "\"can_msg\"\n")
					fw.write("d "+ str(user) +" " + str(i) +" \""+str(line["can_message"])+"\"\n")

