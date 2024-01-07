import time
import googlemaps # pip install googlemaps
import pandas as pd # pip install pandas
import re


class GoogleMapsClient():

    ## List of search queries, inteded to encompass all terms that may be used to reference a particular
    ##  restaurant or bar.
    SEARCH_STRINGS = ['bar', 'restaurant', 'pub', 'night club', 'tavern', 'bistro', 'cafe',
                  'eatery', 'lounge', 'public house', 'drinkery', 'taphouse', 'grill', 
                  'brewery', 'beer', 'alehouse', 'establishment', 'cider'] ## list of search queries

    def __init__(self, api_key):
        self.gmap = googlemaps.Client(key=api_key)
        self.business_list = []
    
    ## Extract top 3 reviews and put them into separate columns
    def extract_reviews(self, reviews):
        if isinstance(reviews, float): # Addresses the float issue
            return ['', '', '']
        review_texts = []
        for review in reviews[:3]:
            review_texts.append(review['text'])
        while len(review_texts) < 3:
            review_texts.append('')
        return review_texts

    ## Extract weekday_text from opening hours and concatenate into one column
    def extract_weekday_text(self, opening_hours):
        if not isinstance(opening_hours, dict) or 'weekday_text' not in opening_hours: # Addresses the float issue
            return ''
        return '|'.join(opening_hours['weekday_text'])

    ## Extract postal code from the 'formatted_address' attribute
    def extract_postal_code(self, address):
        for component in address.split(','):
            component = component.strip()
            match = re.search(r'\b[A-Z][0-9][A-Z] [0-9][A-Z][0-9]\b', component)
            if match:
                return match.group()
        return ''

    # Iterative list generation
    def gen_prospect_list(self, Lat, Long, Radius, file_name):

        self.business_list = []

        # Main Data-building loop.
        for search_string in self.SEARCH_STRINGS:
            response = self.gmap.places_nearby(
                location=(Lat, Long), # Point of query
                keyword=search_string, 
                radius=(Radius * 1000),
                min_price=1,
                max_price=4
            )
            ## Building the data by appending all attributes with some relevance to alcoholic beverage sales
            for place in response['results']:
                place_details = self.gmap.place(
                    place_id=place['place_id'],
                    fields=['name', 
                            'formatted_address', 
                            'formatted_phone_number',
                            'opening_hours',
                            'business_status',
                            'price_level',
                            'reservable', 
                            'delivery', 
                            'dine_in', 
                            'curbside_pickup', 
                            'url',
                            'website',
                            'serves_beer', 
                            'serves_wine',
                            'rating', 
                            'user_ratings_total',
                            'reviews']
                )
                if place_details['result']['business_status'] == 'OPERATIONAL': ## note this does not filter by serves_beer or serves_wine
                    self.business_list.append(place_details['result'])
        
        # Transfer to dataframe
        df = pd.DataFrame(self.business_list)

        # Check if empty
        if df.empty:
            return "No Search Results Error"
        ## Can add elif for other error types.

        else:
            # Build Excel file and return no error
            df = df.drop_duplicates(subset=['name', 'formatted_address'])  # Remove duplicate rows based on name and address
            df['postal_code'] = df['formatted_address'].apply(lambda x: self.extract_postal_code(x) if x else '')
            df[['review_1', 'review_2', 'review_3']] = df['reviews'].apply(lambda x: pd.Series(self.extract_reviews(x)))
            df['weekday_text'] = df['opening_hours'].apply(lambda x: self.extract_weekday_text(x) if x else '')
            df = df.drop(columns=['reviews', 'opening_hours'])
            df.to_excel(f'{file_name}.xlsx', index=False)
            return None  # No error
        


