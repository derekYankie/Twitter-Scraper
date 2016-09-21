import urllib2
from bs4 import BeautifulSoup


#Scrape Donald J. Trump twitter page
theurl = "https://twitter.com/realDonaldTrump"
thepage = urllib2.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

#Get Donald Trump's twitter handle
print (soup.title.text)

#Get Profile stats: tweets following, followers, likes
print(soup.findAll('span',{"class":"ProfileNav-label"}))
print(soup.findAll('span',{"class":"ProfileNav-value"}))




'''for link in soup.findAll('span'):
    print(link.get('class="ProfileNav-label"'))
    print(link.text)'''

#Get 10 most recent tweets


t = 1
for tweets in soup.findAll('div', {"class":"content"}):

    if t <= 10:
        print (t)
        print(tweets.find('p').text)
        t = t + 1