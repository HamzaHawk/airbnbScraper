#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:31:32 2016

@author: abhinandan
"""

import argparse
import pandas as pd
from get_data import scrape_data

def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", required=True, help="Path to the directory that contains the csv file")
    args = parser.parse_args()
    return(args)
    
if __name__ == "__main__":
    args = set_args()

    listing_ids = pd.read_csv(args.p)['id']
    length = len(listing_ids)
    #listing_ids = pd.read_csv('/Users/nandu/desktop/airbnb_scraper/listings.csv')['id']

    listings_data = {}
    df_listings_data = pd.DataFrame(listings_data, index=[0])
    exceptions = {}
    df_exceptions = pd.DataFrame(exceptions, index=[0])
    
    rem = 0
    for _id in listing_ids:
        try:
            listings_data = scrape_data(_id)
            if(listings_data is not None):
                df_listings_data = df_listings_data.append(listings_data, ignore_index=True)
                df_listings_data.to_csv('df_listings_data.csv')
            else:
                raise ValueError("Invalid listing id")
        except Exception as error:
            exceptions['listing_id'] = _id
            exceptions['error_msg'] = error
            df_exceptions = df_exceptions.append(exceptions, ignore_index=True)
            df_exceptions.to_csv('df_exceptions.csv')
        rem+=1
        print("processed %s of %s"%(rem, length))
    print("Completed!")
