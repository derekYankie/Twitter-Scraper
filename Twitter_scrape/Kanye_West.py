import urllib2
from bs4 import BeautifulSoup


#Scrape Kanye West twitter page
theurl = "https://twitter.com/kanyewest"
thepage = urllib2.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

#Get Kanye West's twitter handle
#print (soup.title.text)

''' #Get Profile stats: tweets following, followers, and likes
print(soup.findAll('span',{"class":"ProfileNav-label"}))
print(soup.findAll('span',{"class":"ProfileNav-value"}))'''

#Get both: Twitter handle and profile stats(tweets following, followers, and likes)
person = soup.title.text
print person

for line in soup.find('a'):
    prof_stats = ""
    for data in soup.findAll('a',{"class":"ProfileNav-stat"}):
        prof_stats = prof_stats+ "," + data.text
        print prof_stats

#Get 10 most recent tweets


t = 1
for tweets in soup.findAll('div', {"class":"content"}):

    if t <= 10:
        print (t)
        print(tweets.find('p').text)
        t = t + 1