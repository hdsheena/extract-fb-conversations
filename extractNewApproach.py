"""
Structure of data:
<div class "thread">
	<div class "message">
		<div class "message_header">
			<span class "user"> NEED THIS
			<span class "meta"> NEED THIS
	<p> NEED THIS
	<div class "message">
		<div class "message_header">
			<span class "user"> NEED THIS
			<span class "meta"> NEED THIS
	<p> NEED THIS

"""


import sys
import re
import codecs
#from HTMLParser import HTMLParser
from StringIO import StringIO
import json
import requests
import lxml.etree
import lxml.html
import xml.etree.ElementTree as ET

file = open('messages1.txt', 'r').read()
#file = file1[:50000]+file1[(len(file1)-10000):]
#open('smallmessages.txt', 'w').write(file)



def parse_html(content):
    """
    A possibly safer way to parse HTML content with lxml. This will presumably
    not break on poorly formatted HTML.
    """
    if not isinstance(content, StringIO):
        if not isinstance(content, str) and not isinstance(content, unicode):
            raise Exception("input content must be a str or StringIO instead of " + str(type(content)))
        content = StringIO(content)
    parser = lxml.etree.HTMLParser()
    tree = lxml.etree.parse(content, parser)
    return tree

tree = parse_html(file)
names = []
threads = tree.xpath("//div[contains(@class, 'thread')]")
conversations = {}
#make a list of the user names available to select from, assign correct one to variable
n=0
for thread in threads:
	html = []
	for message in thread:
		if message.keys() == ['class']:
			#html.append("<hr>")
			html.append("<br> Sent by: " + message[0][0].text)
			#html.append(message[0][0].text)
			#html.append("<br>")
			html.append("Date and Time: " +message[0][1].text)
		
		else:
			#html.append("<br>")
			html.append("Message:")
			html.append(message.text)
	conversations[thread.text] = html

courtneyconvos = {}
courtneykey = []
def find_message_content(content,fileout):
	for key in conversations.keys():
		for i in conversations.get(key):	
			if key.find(content) != -1:
				#print i
				print key
				courtneykey.append(key)
				#fileout.write(courtneykey)
		if key in courtneykey:
			fileout.write(key)

def find_person(name,fileout):
	for key in conversations.keys():
		#print key
		if key.find(name) != -1:
			print type(key)
			print type(conversations.get(key))
			courtneykey = key
			#courtneymsg = tuple(conversations.get(key))
			#courtneyconvos[courtneykey] = courtneymsg
			fileout.write("PAGEBREAK")
			fileout.write(courtneykey)
			fileout.write('<hr>')
			for i in conversations.get(key):	
				fileout.write(i.encode('utf-8'))
				fileout.write("<br>")
			#courtneyconvos.update({courtneykey, courtneymsg})
			print key
			#print conversations.get(key)
			#print "True"


cfile0 = open('keys.txt', 'w')
find_message_content('Courtney',cfile0)
print>>cfile0, conversations.keys()
#find_person('537679397',cfile0)
sfile0 = open('courtneyconvosnamed.txt', 'w')
#find_person('Courtney',sfile0)
