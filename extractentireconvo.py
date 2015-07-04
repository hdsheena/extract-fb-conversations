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

#make a list of the user names available to select from, assign correct one to variable
for thread in threads:
	names.append(thread.text)
	if thread.text == "REPLACEDUSERNAMES":
		courtenaythread = thread

html = []
messages = courtenaythread.xpath("//div[text()[contains(., 'REPLACEDUSERNAMES')]]/*")

for message in messages:
	#while n < 50:
	#print message.keys()
	if message.keys() == ['class']:
		html.append("<hr>")
		html.append("Sent by")
		html.append(message[0][0].text)
		html.append("<br>")
		html.append("Date and Time")
		html.append(message[0][1].text)
		
	else:
		html.append("<br>")
		html.append("Message:")
		html.append(message.text)
		#n =+ 1

	#html.append(message[0][0].text)
	#html.append(message[0][1].text)
	#html.append(message.text)

#from here up works, but need to split the file so its more manageable
n=0
i=0
while n < len(html):
	print "cfile"+str(i)+"= open('courtenaymsgs"+str(i)+".txt', 'w')"
	print "print>>cfile"+str(i)+", html["+str(n)+":"+str(n+12000)+"]"
	n= n+12000
	i= i+1

cfile0 = open('courtenaymsgs0.txt', 'w')
print>>cfile0, html[0:12000]
cfile1= open('courtenaymsgs1.txt', 'w')
print>>cfile1, html[12000:24000]
cfile2= open('courtenaymsgs2.txt', 'w')
print>>cfile2, html[24000:36000]
cfile3= open('courtenaymsgs3.txt', 'w')
print>>cfile3, html[36000:48000]
cfile4= open('courtenaymsgs4.txt', 'w')
print>>cfile4, html[48000:60000]
cfile5= open('courtenaymsgs5.txt', 'w')
print>>cfile5, html[60000:72000]
cfile6= open('courtenaymsgs6.txt', 'w')
print>>cfile6, html[72000:84000]
cfile7= open('courtenaymsgs7.txt', 'w')
print>>cfile7, html[84000:96000]
cfile8= open('courtenaymsgs8.txt', 'w')
print>>cfile8, html[96000:108000]
cfile9= open('courtenaymsgs9.txt', 'w')
print>>cfile9, html[108000:120000]
cfile10= open('courtenaymsgs10.txt', 'w')
print>>cfile10, html[120000:132000]
cfile11= open('courtenaymsgs11.txt', 'w')
print>>cfile11, html[132000:144000]
cfile12= open('courtenaymsgs12.txt', 'w')
print>>cfile12, html[144000:156000]
cfile13= open('courtenaymsgs13.txt', 'w')
print>>cfile13, html[156000:168000]
cfile14= open('courtenaymsgs14.txt', 'w')
print>>cfile14, html[168000:180000]
cfile15= open('courtenaymsgs15.txt', 'w')
print>>cfile15, html[180000:192000]
cfile16= open('courtenaymsgs16.txt', 'w')
print>>cfile16, html[192000:204000]
cfile17= open('courtenaymsgs17.txt', 'w')
print>>cfile17, html[204000:216000]


"""
cfile = open('courtenaymsgs.txt', 'w')

for i in html:
	print>>cfile, i.encode('utf-8')

print>>cfile, messages
print courtenaythread.text
"""