# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import json
import time
import pkg_resources

import six
from six.moves.urllib.parse import urlencode
import requests
from git.response import gitResponse

from git.settings import DEFAULT_BASE_URL_FOR_TEXT

class Endpoint(object):
	
	def __init__(self,accountId,apikey,emailId, base_url=DEFAULT_BASE_URL_FOR_TEXT):

		self.accountId = accountId
		self.apikey = apikey
		self.emailId = emailId
		self.base_url = base_url
	
	
	
class Classifications(Endpoint):
	def sentiment(self, data):


		#url = '{}'.format(self.base_url)+"/"+"sentiment"+"/"+'{}'.format(self.accountId)+"/"+'{}'.format(self.apikey)+"/"+'{}'.format(self.emailId)+"?userinputdata="+data

		response=gitResponse()
		
		raw_responses = requests.get(self.base_url,verify=False)

		response.add_raw_response(raw_responses)

		return response

	
		raw_responses = requests.get(url, data,verify=False)
		
		response.add_raw_response(raw_responses)

		return response

	def readability(self, data):


		url = '{}'.format(self.base_url)+"/"+"readability"+"/"+'{}'.format(self.accountId)+"/"+'{}'.format(self.apikey)+"/"+'{}'.format(self.emailId)+"?userinputdata="+data

		response=data2InsightsResponse()

		raw_responses = requests.get(url, data,verify=False)
		
		response.add_raw_response(raw_responses)

		return response
	

	def similarity(self, data1,data2):


		url = '{}'.format(self.base_url)+"/"+"similarity"+"/"+'{}'.format(self.accountId)+"/"+'{}'.format(self.apikey)+"/"+'{}'.format(self.emailId)+"/"+data1+"/"+data2

		response=data2InsightsResponse()

		raw_responses = requests.get(url,verify=False)
		
		response.add_raw_response(raw_responses)

		return response

	def bertentity(self,data):

		url = '{}'.format(self.base_url)+"/"+"bertentity"+"/"+'{}'.format(self.accountId)+"/"+'{}'.format(self.apikey)+"/"+'{}'.format(self.emailId)+"?userinputdata="+data
		
		response=data2InsightsResponse()

		raw_responses = requests.get(url,data,verify=False)

		response.add_raw_response(raw_responses)

		return response

	def hemptopic(self,data):
		
		url = "{}".format(self.base_url)+"/"+"hemptopic"+"/"+"{}".format(self.accountId)+"/"+'{}'.format(self.apikey)+"/"+'{}'.format(self.emailId)+"?userinputdata="+data

		response=data2InsightsResponse()

		raw_responses = requests.get(url,data,verify=False)
		
		response.add_raw_response(raw_responses)

		return response

	def summarization(self,data):
	
		url = "{}".format(self.base_url)+"/"+"summarization"+"/"+"{}".format(self.accountId)+"/"+'{}'.format(self.apikey)+"/"+'{}'.format(self.emailId)+"?userinputdata="+data

		response=data2InsightsResponse()

		raw_responses = requests.get(url,data,verify=False)
		
		response.add_raw_response(raw_responses)

		return response
		
	def QA(self,question,paragraph):
		
		url = "{}".format(self.base_url)+"/"+"Q&A"+"/"+"{}".format(self.accountId)+"/"+'{}'.format(self.apikey)+"/"+'{}'.format(self.emailId)+"?question="+question+"&paragraph="+paragraph

		response=data2InsightsResponse()

		raw_responses = requests.get(url,question,verify=False)
		
		response.add_raw_response(raw_responses)

		return response
