from geopy.geocoders import Nominatim
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
#### Create geolocator object
geolocator = Nominatim(user_agent="http://odisee.be")
#### Enter city and country
city_country = "Ukkel, Belgium"
#### Search location (latitude, longitude)
location = geolocator.geocode(city_country)
print(location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
print((devnet_lat, devnet_lon))