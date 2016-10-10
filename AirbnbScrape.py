#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:00:50 2016

@author: abhinandan
"""

import requests
from bs4 import BeautifulSoup

class AirbnbScraper(object):
    
    def __init__(self, _id):
        self.url = 'https://www.airbnb.com/rooms/'+_id
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "lxml")
        page_title = soup.title.text
        if(not(page_title.startswith('Top 20')) and not(page_title.startswith('Page not found'))):
            self.soup = soup
        else:
            self.soup = None
                
    def get_listing_name(self):
        '''
            returns the name of the listing.
        '''
        listing_name = self.soup.find(name="h1", attrs={"id":"listing_name"}).text.encode('utf-8')
        return(listing_name)
        
    def get_host_name(self):
        '''
            returns the name of the listing's host.
        '''
        host_name = self.soup.find(name="a", attrs={"href":"#host-profile", "class":"link-reset text-wrap"}).text.encode('utf-8')
        return(host_name)

    def get_number_of_reviews(self):
        '''
            returns the number of reviews for the listing.
        '''
        span = self.soup.find(name="span", attrs={"itemprop":"reviewCount"})
        if(span is not None):
            number_of_reviews = int(span.text.encode('utf-8'))
            return(number_of_reviews)
        else:
            return(0)
    
    def get_rating(self):
        '''
            returns the current rating of the listing.
        '''
        div = self.soup.find(name="div", attrs={"class":"star-rating", "itemprop":"ratingValue"})
        if(div is not None):
            rating = float(div['content'].encode('utf-8'))
            return(rating)
        else:
            return(None)
    
    def get_neighborhood(self):
        '''
            returns the neighborhood of the listing.
        '''
        neighborhood = self.soup.find(name="a", attrs={"href":"#neighborhood", "class":"link-reset"}).text.encode('utf-8')
        return(neighborhood)

    def get_price(self):
        '''
            returns the price of the listing.
        '''
        price = float(self.soup.find(name="span", attrs={"class":"h3"}).text.encode('utf-8').strip('$'))
        return(price)
    
    def is_instant_book(self):
        '''
            returns 1 if the Instant Book option is available for the listing, 0 otherwise.
        '''
        isInstantBook = 1 if(self.soup.find(name="i", attrs={"class":"icon icon-instant-book icon-beach h4 book-it__instant-book-price-icon"}) is not None) else 0
        return(isInstantBook)

    def is_superhost(self):
        '''
            returns 1 if the listing's host is a Super Host, 0 otherwise.
        '''
        isSuperHost = 1 if(self.soup.find(name="img", attrs={"class":"superhost-photo-badge superhost-photo-badge"}) is not None) else 0
        return(isSuperHost)  
        
    def is_verified(self):
        '''
            returns 1 the listing's host has a verified profile on Airbnb, 0 otherwise.
        '''
        isVerified = 1 if(self.soup.find(name="img", attrs={"alt":"Verified"}) is not None) else 0
        return(isVerified)

    def get_review_scores(self): 
        '''
            returns the review scores of the listing.
        '''
        scores_list = []
        div = self.soup.find(name="div", attrs={"class":"review-inner space-top-2 space-2"})
        if(div is not None):
            divs = div.find_all(name="div", attrs={"class":"col-lg-6"})
            for div in divs: 
                for child in div.children:
                    key = child.text.encode('utf-8').strip()
                    value = child.find(name="div", attrs={"class":"star-rating"})['content']
                    scores_list.append({key:value})
            return(scores_list)
        else: 
            return(None)
    
    def get_count_saved(self):
        '''
            returns the count of the number of travelers who've saved the listing.
        '''
        span = self.soup.find(name="span", attrs={"class":"wishlist-button-subtitle-text"})
        if(span is not None):
            count_saved = int(span.text.encode('utf-8').strip(' travelers saved this place\n'))
            return(count_saved)
        else:
            return(0)
    
        
    def get_details(self, tag):
        '''
            if the argument 'tag' is set to "prices", the method returns the details of the 'Prices' section of the page. 
            Details of "The Space" section are returned otherwise.
        '''
        index = 2 if(tag == "prices") else 0
        details = {}
        price_list = self.soup.find_all(name="div", attrs={"class":"col-md-3 text-muted"})[index].find_next_siblings("div")[0]
        for i in price_list.select("div > div > div"):
            text = i.text.encode('utf-8').split(':')
            details[text[0]] = text[1].strip()
        return(details)

    def get_availability(self):
        '''
            returns the minimum nights stay
        '''
        divs = self.soup.find_all(name="div", attrs={"class":"col-md-3 text-muted"})
        for div in reversed(divs):
            if(div.text.encode('utf-8')=="Availability"):
                sibling = div.find_next_siblings("div")[0]
                availability = int(sibling.select("strong")[0].text.encode('utf-8').strip(" nights"))
                return(availability)


                
scraper = AirbnbScraper('755528')
scraper = AirbnbScraper('12791130')

scraper.get_review_scores()




page = requests.get('https://www.airbnb.com/rooms/4116501abcd')

soup = BeautifulSoup(page.content, "lxml")


