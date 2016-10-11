#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:35:16 2016

@author: abhinandan
"""
import argparse
from AirbnbScrape import ListingScraper
 
def scrape_data(_id):
    d = {}
    scraper = ListingScraper(str(_id))
    if(scraper.soup is not None):
        d['url'] = scraper.url
        d['listing_id'] = _id
        d['listing_name'] = scraper.get_listing_name()
        d['host_name'] = scraper.get_host_name()
        d['number_of_reviews'] = scraper.get_number_of_reviews()
        d['rating'] = scraper.get_rating()
        d['price'] = scraper.get_price()
        d['neighborhood'] = scraper.get_neighborhood()
        d['verified'] = scraper.is_verified()
        d['superhost'] = scraper.is_superhost()
        d['instant_book'] = scraper.is_instant_book()
        d['count_saved'] = scraper.get_count_saved()
        d['availability'] = scraper.get_availability()
        
        review_scores = scraper.get_review_scores()
        if(review_scores is not None):
            d['_accuracy'] = review_scores['Accuracy']
            d['_communication'] = review_scores['Communication']
            d['_cleanliness'] = review_scores['Cleanliness']
            d['_location'] = review_scores['Location']
            d['_checkin'] = review_scores['Check In']
            d['_value'] = review_scores['Value']
        price_details = scraper.get_details("prices")
        if(price_details is not None):
            d['cancellation'] = price_details['Cancellation'] if('Cancellation' in price_details.keys()) else None
            d['__cleaning-fee'] = float(price_details['Cleaning Fee'].strip('$')) if('Cleaning Fee' in price_details.keys()) else None

        space_details = scraper.get_details("space")
        if(space_details is not None):
            d['__accommodates'] = float(space_details['Accommodates']) if('Accommodates' in space_details.keys()) else None
            d['__bathrooms'] = float(space_details['Bathrooms']) if('Bathrooms' in space_details.keys()) else None
            d['__bedrooms'] = float(space_details['Bedrooms']) if('Bedrooms' in space_details.keys()) else None
            d['__beds'] = float(space_details['Beds']) if('Beds' in space_details.keys()) else None
            d['__check-in'] = space_details['Check In'] if('Check In' in space_details.keys()) else None
            d['__property-type'] = space_details['Property type'] if('Property type' in space_details.keys()) else None
            d['__room-type'] = space_details['Room type'] if('Room type' in space_details.keys()) else None
        return(d)
    else:
        return(None)
