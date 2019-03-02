'''
 * This module will use twitter JSON File and convert the JSON data into a graph
 * This graph file is used by GBAD to find the anomaly detection later on
 * Python Version 2.7
 *
 *
 * @Layer      		DataProcessing Layer
 * @Module     		Twitter Parser Module
 * @Author     		Ramesh Paudel <rpaudel42@students.tntech.edu>
 * @LastModifiedDate 	April 08 2014
'''

import json, sys,getopt
import os,glob

class TwitterParser():

	def __init__(self):
		print "\n\n ---- Starting Twitter Parser ---"

	def twitter_parser(argv):
		source =''
		dest =''
		try:
			opts,args = getopt.getopt(argv,"hs:g:",["source=","graph="])
		except getopt.GetoptError:
			print 'twparser.py -s <SOURCE FILE> -g <GRAPH FILE>'
			sys.exit(2)

		for opt, arg in opts:
			if opt == '-h':
				print 'twparser.py -s <SOURCE FILE> -g <GRAPH FILE>'
				sys.exit();
			elif opt in("-s", "--source"):
				source = arg;
			elif opt in("-g", "--graph"):
				dest = arg;

		#source = "Graph/obamaegypt.g";
		fw = open(dest, "a")
	   # dest = 'JSON/twitter'

		with open(source) as fp:

			j=1
			for line in fp:
				line = line.strip()
				data = ''
				try:
					data = json.loads(line)
				except ValueError as detail:
				#	sys.stderr.write(detail.__str__() + "\n")
					continue
				fw.write("XP # "+str(j)+"\n")
				j = j+1
				i=0
				if (data['id'] is not None ):
					i = i+1
					fw.write("v "+ str(i) +" \"text\"\n")
					text=i
				if (data['lang'] is not None ):
					i = i+1
					fw.write("v "+ str(i) + "\""+data['lang']+"\"\n")
					fw.write("d "+ str(i-1) +" " + str(i) +" \"lang\"\n")

					if (data['user']['id'] is not None ):
						i = i+1
						fw.write("v "+ str(i) +" \"user\"\n")
						user=i
						userDict ={ i: data['user']['id_str']}
					if (data['user']['time_zone'] is not None ):
						i=i+1
						fw.write("v "+ str(i) + "\"" + data['user']['time_zone']+"\"\n")
						fw.write("d "+ str(i-1) +" " + str(i) +" \"tz\"\n")
						fw.write("d "+ str(user) +" " + str(text) +" \"tweet\"\n")
					if (data['user']['lang'] is not None ):
						i = i+1
						fw.write("v "+ str(i) + "\""+data['user']['lang']+"\"\n")
						fw.write("d "+ str(user) +" " + str(i) +" \"lang\"\n")


					#tracking user mentioned in the status..................

					if 'entities' in data and len(data['entities']['user_mentions']) > 0:
						user_mentions = data['entities']['user_mentions']
						for u2 in user_mentions:
							if(u2['id'] is not None):
								i = i+1
								umention = i
								fw.write("v "+ str(i) +" \"user\"\n")
							if(u2['id_str'] is not None):
								#i = i+1
								fw.write("d "+ str(user) +" " + str(umention) +" \"mention\"\n")

						#tracking retweeted status............
						retext = 0
						reuser = 0

						if 'retweeted_status' in data > 0:
							retweet = data['retweeted_status']
							if (retweet['id'] is not None ):
								i = i+1
								fw.write("v "+ str(i) +" \"text\"\n")
								retext=i
							if (retweet['lang'] is not None ):
								i = i+1
								#textDict = {i: data['id_str']}
								fw.write("v "+ str(i) + "\""+retweet['lang']+"\"\n")
								fw.write("d "+ str(i-1) +" " + str(i) +" \"lang\"\n")
							if (retweet['user']['id'] is not None ):
								i = i+1
								fw.write("v "+ str(i) +" \"user\"\n")
								reuser=i
								#userDict ={ i: data['user']['id_str']}
							if (retweet['user']['time_zone'] is not None ):
								i=i+1
								fw.write("v "+ str(i) + "\""+retweet['user']['time_zone']+"\"\n")
								fw.write("d "+ str(i-1) +" " + str(i) +" \"tz\"\n")
								fw.write("d "+ str(reuser) +" " + str(retext) +" \"tweet\"\n")
							if (retweet['user']['lang'] is not None ):
								i = i+1
								fw.write("v "+ str(i) + "\""+retweet['user']['lang']+"\"\n")
								fw.write("d "+ str(reuser) +" " + str(i) +" \"lang\"\n")
							if (retext >0):
								fw.write("d "+ str(retext) +" " + str(text) +" \"retweet\"\n")
		fw.close()