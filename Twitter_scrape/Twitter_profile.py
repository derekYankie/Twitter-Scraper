import urllib2
from bs4 import BeautifulSoup

#Accept user twitter profile link
while True:
	theurl = raw_input('Enter a twitter profile link \n(Ex1) https://twitter.com/[twitterhandle]\n(Ex2)Twitter handle: @nytimes @CNN @WSJ \n Link:https://twitter.com/nytimes: ')
	if len(theurl)> 1 : break

#Scrape selected twitter page
thepage = urllib2.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

#Get both: Twitter handle and profile stats(tweets following, followers, and likes)
person = soup.title.text
print person

#Get Profile stats
profile_stats = soup.findAll("a", { "class":"ProfileNav-stat"})
#ConvertUnicode string into the Python ASCII and remove /n character
stats = [d.text.encode('utf-8').split() for d in profile_stats]
print "Stats>>",stats


#Get 15 most recent tweets
print "Their 15 most recent tweets... "
t = 1
for tweets in soup.findAll('div', {"class":"content"}):

    if t <= 15:
        print (t)
        print(tweets.find('p').text)
        t = t + 1

#Python GUI: Displays selected twitter page stats
from Tkinter import *

root = Tk()
root.title("Twitter Scapper Widget")
T = Text(root, height=30, width=50)
T.pack()
T.insert(END, stats)
mainloop()