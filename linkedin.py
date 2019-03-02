'''
 * This module will use LinkedIn API to get the data from LinkedIn. We send 
 * the data request using URL request and get the data back from LinkedIn
 * Python Version 2.7
 *
 *
 * @Layer      		DataExtraction Layer
 * @Module     		LinkedAPI Call Module
 * @Author     		Ramesh Paudel <rpaudel42@students.tntech.edu>
 * @LastModifiedDate 	April 08 2014
'''

import oauth2 as oauth #pip install oauth2
import sys,getopt,time,json
import requests

# Define CONSUMER_KEY, CONSUMER_SECRET,
# USER_TOKEN, and USER_SECRET from the credentials
# provided in your LinkedIn application
class LinkedIn():
	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''
	USER_TOKEN = ''
	USER_SECRET = ''

	def __init__(self):
		print "\n\n ---- Starting LinkedIn API Call ---"

		CONSUMER_KEY = '<consumer key>'
		CONSUMER_SECRET = '<consumer secret>'
		USER_TOKEN = '<user token>'
		USER_SECRET = '<user secret>'

	def call_linkedin_api(argv):

		#initialize field value. the field variable will hold the field user enter through
		#command line. The field are the data field of LinkedIn users

		field=''

		#Get user input from command line
		#The user input are data field of LinkedIn users

		try:
			opts,args = getopt.getopt(argv,"hf:",["field="])
		except getopt.GetoptError:
			print 'linkedin.py -f <fields like "a,b,c">'
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				print 'linkedin.py -f <fields like "a,b,c">'
				sys.exit();
			elif opt in("-f", "--field"):
				field = arg;

		url = "http://api.linkedin.com/v1/people/~/connections:(" + field + ")?format=json"
		#url = "http://api.linkedin.com/v1/people/~/connections?format=json"
		#print url
		user = oauth.Consumer(key=self.CONSUMER_KEY,secret =self.CONSUMER_SECRET)
		token = oauth.Token(key=self.USER_TOKEN,secret = self.USER_SECRET)

		client= oauth.Client(user,token)
		resp,content = client.request(url)
		#content1 = requests.get(url).json()

		# Write JSON data in the file
		newGraphFile = 'JSON/linkedin/lk' +'.'+ time.strftime('%Y%m%d-%H%M%S') + '.json';
		fw = open(newGraphFile, "a")
		fw.write(content)
		fw.close

		data = json.loads(content)
		nodeCount = 0
		for line in data["values"]:
			nodeCount = nodeCount + 1
			print nodeCount," item extracted ....."
			time.sleep(0.1)
		print "Total ",str(nodeCount),"profile are extracted. Please check the folder for the file"

