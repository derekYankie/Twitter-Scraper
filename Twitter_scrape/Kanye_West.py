import urllib2
from bs4 import BeautifulSoup



theurl = "https://twitter.com/kanyewest"
thepage = urllib2.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

#Get Kanye West's twitter handle
print (soup.title.text)

#Get Profile stats: tweets following, followers, and likes
print(soup.findAll('span',{"class":"ProfileNav-label"}))
print(soup.findAll('span',{"class":"ProfileNav-value"}))



#Get 10 most recent tweets
t = 1
for tweets in soup.findAll('div', {"class":"content"}):

    if t <= 10:
        print (t)
        print(tweets.find('p').text)
        t = t + 1