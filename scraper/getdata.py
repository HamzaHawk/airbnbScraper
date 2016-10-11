import argparse
from scrape import scrape_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", required=True, help="Airbnb listing id")
    args = parser.parse_args()
    
    x = scrape_data(args.i)
    for a,b in enumerate(x):
        print a,b,' : ',x[b]
