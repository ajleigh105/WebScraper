#usiong urllib and regex. Scrapes a single element from google finance (Apple Stock price)
import urllib, re
#grab the "get" request from google finances
html_text = urllib.urlopen("https://www.google.com/finance/getprices?q=AAPL&x=NASD&i=1800&p=30d&f=d,c,v,o,h,l&df=cpct&auto=1&ts=1475047464400&ei=V23rV9HhONbfjAGarK-4Cw").read()
#cut it up for easy reading
cut_text = html_text.split()[len(html_text.split())-1][:-8]
stocknum = cut_text[24:]
#print the results
print stocknum

waitkey = raw_input()

