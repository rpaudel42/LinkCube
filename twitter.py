'''
 * This module will use Twitter Streaming API to get the data from twitter. We send 
 * the data request using specific keyword and get the data back from Twitter
 * Python Version 2.7
 *
 *
 * @Layer      		DataExtraction Layer
 * @Module     		Twitter API Call Module
 * @Author     		Ramesh Paudel <rpaudel42@students.tntech.edu>
 * @LastModifiedDate 	April 08 2014
'''

from slistener import SListener
import time, tweepy, sys, getopt
import getpass

class Twitter():
	def __init__(self):
		print "\n\n ---- Starting Twitter API Call ---"

	def call_twitter_api(argv):
		## the username and password fields to authenticate from Twitter.
		username = '';
		password = '';
		track  = ['']

		#Get user input from command line
		#The user input are twitter username and tweet keyword
		#Tweet keyword is used to extract tweet stream
		#User have to provide their password to get the result back

		try:
			opts,args = getopt.getopt(argv,"hu:t:",["uname=","tweet="])
		except getopt.GetoptError:
			print 'twitter.py -u <username>  -t <tweet_keyword>'
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				print 'twitter.py -u <username> -t <tweet_keyword>'
				sys.exit();
			elif opt in("-u", "--uname"):
				username = arg;
			elif opt in("-t", "--tweet"):
				track = [arg];

		#ask for the twitter account password.. This is for autheticating the user
		password = getpass.getpass()

		#initialize authentication handler
		auth     = tweepy.auth.BasicAuthHandler(username, password)

		#Authenticate twitter API using the authentication handler
		api      = tweepy.API(auth)

		#keys and token from twitter api
		consumer_key        = "<custemer key>"
		consumer_secret     = "<custemer secrete>"
		access_token        = "<access token>"
		access_token_secret = "<access token secret>"

		# OAuth process, using the keys and tokens
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

			follow = []

		listen = SListener(api, 'test')
		stream = tweepy.Stream(auth, listen)

		#Displaying the status of data extraction
		print "Streaming started on Keyword = "+track[0];
			try:
				stream.filter(track = track, follow = follow)

			except:
				print "error!"
				stream.disconnect()

