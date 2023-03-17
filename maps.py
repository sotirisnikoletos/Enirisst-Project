import pandas as pd
import googlemaps

API_KEY='AIzaSyD5ruHJBYj_HTfTOBQJM80YoGzgSSw1IQw'


gmaps = googlemaps.Client(key=API_KEY)
df = pd.read_csv('thebest_tokenized_stopwords.csv')




def get_lat(address, lat_range=None):
    if pd.isnull(address) or address == "":
        return None, None
    else:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            lat = geocode_result[0]['geometry']['location']['lat']
            if (lat_range is None or lat_range[0] <= lat <= lat_range[1]):
                return lat
            else:
                return None
        else:
            return None



def get_long(address, lng_range=None):
    if pd.isnull(address) or address =="":
        return None,None
    else:
        geocode_result = gmaps.geocode(address)
        if geocode_result:

            lng = geocode_result[0]['geometry']['location']['lng']
            if(lng_range is None or lng_range[0] <= lng <= lng_range[1]):
                return lng
            else:
                return None
        else:
            return None
lat_range = (38.17782615060196, 38.31901406495858)
lng_range = (21.684319147603844, 21.815663152685588)

# Apply the function to your pandas column to get the latitude and longitude
df['latitude'] = df['Location'].apply(get_lat, lat_range=lat_range)
df['longitute']=df['Location'].apply(get_long, lng_range=lng_range)

# Save the updated DataFrame to a new CSV file
df.to_csv('thebest_lat_long.csv', index=False)