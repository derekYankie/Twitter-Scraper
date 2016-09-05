import urllib2
from bs4 import BeautifulSoup



theurl = "https://twitter.com/kanyewest"
thepage = urllib2.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

#Get Kanye West's twitter handle
#print (soup.title.text)

''' #Get Profile stats: tweets following, followers, and likes
print(soup.findAll('span',{"class":"ProfileNav-label"}))
print(soup.findAll('span',{"class":"ProfileNav-value"}))'''

#Get both: Twitter handle and profile stats
person = soup.title.text
prof_stats = ""
for labels in soup.findAll('a',{"class":"ProfileNav-stat"}):
    prof_stats = prof_stats + "," + labels.text
    print person + prof_stats

