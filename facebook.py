'''
 * This module will use facebook graph API to get the data from facebook. We send 
 * the FQL query using URL request and get the data back from facebook
 * Python Version 2.7
 *
 *
 * @Layer      		DataExtraction Layer
 * @Module     		Facebook FQL Request Module
 * @Author     		Ramesh Paudel <rpaudel42@students.tntech.edu>
 * @LastModifiedDate 	April 08 2014
'''


#import required module to work with Facebook
import requests # pip install requests
import json 
import facebook #pip install facebook-sdk
import sys, getopt,time
import urllib,time
class Facebook():

	def __init__(self):
		print "\n\n ---- Starting Facebook API Call ---"

	def call_facebook_api(argv):

		#Initializing variable for ACCESS_TOKEN and FQL

		ACCESS_TOKEN = ''
		query = '' # 'select name,can_post,can_message, locale from user where uid IN (SELECT uid2  from friend where uid1 = 514904299)'

		#Get user input from command line
		#The user input are ACCESS_TOKEN of an individual user and the FQL based on the data requirement

		try:
			opts, args = getopt.getopt(argv,"ha:q:",["atok=","query="])
		except getopt.GetoptError:
			print 'facebook.py -a <ACCESS_TOKEN> -q <"QUERY">'
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				print 'facebook.py -a <ACCESS_TOKEN> -q <"QUERY">'
				sys.exit()
			elif opt in ('-a', '--atok'):
				ACCESS_TOKEN = arg;
			elif opt in ('-q', '--query'):
				query = arg;

			#Format query for the URL
		query = urllib.quote(query)

		#Initialize base URL for facebook graph
		base_url = "https://graph.facebook.com/fql"

		#2nd part of URL for facebook graph with appended ACCESSTOKEN and FQL
		url = '%s?q=%s&access_token=%s' % \
			(base_url, query, ACCESS_TOKEN,)

		#send FQL request using request module
		content = requests.get(url).json()

		#This command will print the data received from facebook API
		#print content

		nodeCount = 0
		for fields in content['data']:
			nodeCount = nodeCount + 1
			print nodeCount," item extracted ....."
			time.sleep(0.01)

		print "Total ",str(nodeCount)," profile are extracted. Please check the folder for the file"

		# Write JSON data in the file
		newGraphFile = 'JSON/facebook/fb' +'.'+ time.strftime('%Y%m%d-%H%M%S') + '.json';
		fw = open(newGraphFile, "a")
		fw.write(json.dumps(content, indent=1))


   
   





