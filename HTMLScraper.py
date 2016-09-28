#usiong urllib and regex. Scrapes websites' htmnl code and website title data
import urllib, re

#any urls in these brackets will be used in the code execution
urls = ["http://google.com", "http://yahoo.com", "http://youtube.com", "http://twitter.com"]
regex_title = '<title>(.+?)</title>'
pattern_title = re.compile(regex_title)
data_file = open("Scrape data.txt", "w")
#make our file blank so we can put our new data in
data_file.truncate()

#main loop
for  url in urls:
    #opens the url for reading
    html_code = urllib.urlopen(url)
    html_text = html_code.read()
    #sorts out the pieces that we actually want
    title_text = re.findall(pattern_title,html_text)
    #writes those pieces to the file
    data_file.write("TITLE:\n" + str(title_text) + "\nHTML:\n" + str(html_text)) 

#finishing steps
data_file.close
print "Scraping completed"
waitkey = raw_input()
