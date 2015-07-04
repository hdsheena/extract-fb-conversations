import sys
import re
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

correct_sender = []

"""
Desired format of dictionary:
Each message will have a header, which contains the user and meta, and a content.
{item1, item2}
where item1 == [user,meta],content
"""

#add to dictionary


def get_messages_from():
	threads = tree.xpath("//div[contains(@class, 'thread')]")
	for thread in threads:
		for msg in thread:
			msg.xpath("//div[contains(@class, 'message')]")
			message = msg.xpath("//div[contains(@class, 'message_header')]")
			#print "Next Message _____"
			#print message
			#print message[0].xpath("//span")
		#for message in messages:
			#if "Jude" in message.text:
			#correct_sender.append(message.root)
			#print "found one"
			#print message.xpath("//span[contains(@class, 'user')]")		
	return threads

#print correct_sender
#for spantag in correct_sender:
	#print spantag.text


tree = parse_html(file)
get_messages_from()

threads = tree.xpath("//div[contains(@class, 'thread')]")
for thread in threads:
	print thread.text
	if thread.text == "REPLACEDUSERNAMES":
		courtenaythread = thread
print courtenaythread







