#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:00:50 2016

@author: nandu
"""

import requests
from bs4 import BeautifulSoup

class AirbnbScraper(object):
    
    def __init__(self, id):
        #add exception handling
        self.url = 'https://www.airbnb.com/rooms/'+id
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.content, "lxml")
        
    def get_listing_name(self):
        listing_name = self.soup.find(name="h1", attrs={"id":"listing_name"}).text.encode('utf-8')
        return(listing_name)
        
    def get_host_name(self):
        host_name = self.soup.find(name="a", attrs={"href":"#host-profile", "class":"link-reset text-wrap"}).text.encode('utf-8')
        return(host_name)

    def get_number_of_reviews(self):
        number_of_reviews = int(self.soup.find(name="span", attrs={"itemprop":"reviewCount"}).text.encode('utf-8'))
        return(number_of_reviews)
    
    def get_rating(self):
        rating = float(self.soup.find(name="div", attrs={"class":"star-rating", "itemprop":"ratingValue"})['content'].encode('utf-8'))
        return(rating)
    
    def get_neighborhood(self):
        neighborhood = self.soup.find(name="a", attrs={"href":"#neighborhood", "class":"link-reset"}).text.encode('utf-8')
        return(neighborhood)

    def get_price(self):
        price = float(self.soup.find(name="span", attrs={"class":"h3"}).text.encode('utf-8').strip('$'))
        return(price)
    
    def is_instant_book(self):
        isInstantBook = 1 if(self.soup.find(name="i", attrs={"class":"icon icon-instant-book icon-beach h4 book-it__instant-book-price-icon"}) is not None) else 0
        return(isInstantBook)

    def is_superhost(self):
        isSuperHost = 1 if(self.soup.find(name="img", attrs={"class":"superhost-photo-badge superhost-photo-badge"}) is not None) else 0
        return(isSuperHost)  
        
    def is_verified(self):
        isVerified = 1 if(self.soup.find(name="img", attrs={"alt":"Verified"}) is not None) else 0
        return(isVerified)

    def get_review_scores(self):       
        scores_list = []
        review = self.soup.find(name="div", attrs={"class":"review-inner space-top-2 space-2"})
        review_scores = review.find_all(name="div", attrs={"class":"col-lg-6"})
        for item in review_scores: 
            for child in item.children:
                key = child.text.encode('utf-8').strip()
                value = child.find(name="div", attrs={"class":"star-rating"})['content']
                scores_list.append({key:value})
        return(scores_list)

        
scraper = AirbnbScraper('755528')

scraper.get_review_scores()

scraper.get_number_of_reviews()



scraper.soup.findChild(name="span")

page = requests.get('https://www.airbnb.com/rooms/755528')
soup = BeautifulSoup(page.content, "lxml")
soup.get

for i in soup.find_all(name="div", attrs={"class":"col-md-9 expandable"}):
    print i, '\n\n'



div1 = soup.find_all(name="div", attrs={"class":"row amenities"})

expandable = div1[0].find_all(name="div", attrs={"class":"col-md-9 expandable"})

expandable_full = expandable[0].find_all(name="div", attrs={"class":"expandable-content expandable-content-full"})

for i in expandable:
    print i.prettify()
    print '\n\n'

    

    
    
    
    
    
    
    
l = []
l.append({'Check In':4.5})
