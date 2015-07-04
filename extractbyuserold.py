
file1 = open('messages1.txt', 'U').read()
file = file1[723000:733240]
open('shortmessagescourtenay.txt', 'w').write(file)
"""
#was using html parser but decided to try lxml instead

file = open('messages1.txt', 'U').read()
file = file1[50000:70000]
print file
message_positions = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        starttag = tag
    def handle_endtag(self, tag):
        endtag = tag
    def handle_data(self, data):
        if data.find("Courtenay Watson"):
		position = self.getpos()
		message_positions.append(position)
		#print data[position:(position+10)]
		

parser = MyHTMLParser()
parser.feed(file)


print message_positions
"""




#find string in file, and print 50 characters before and 500 after the first letter of that string
first_incidence = file.find("<span class=\"user\">Courtenay Watson</span>")
context_before = first_incidence - 50
context_after = first_incidence + 500
print first_incidence

#use the number found above to search for the "next" incidence of that string and return
file_second = file[context_after:]
second_incidence = file_second.find("<span class=\"user\">Courtenay Watson</span>")
context_before = second_incidence - 50
context_after = second_incidence + 500
#print file[context_before:context_after]
