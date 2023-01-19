from geopy.geocoders import Nominatim
import folium
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
#### Create geolocator object
geolocator = Nominatim(user_agent="http://odisee.be")
#### Enter city and country
city_country = "Brussels, Belgium"
#### Search location (latitude, longitude)
location = geolocator.geocode(city_country)
print(location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
print((devnet_lat, devnet_lon))
#### Print map of the location
coordinates = [devnet_lat,devnet_lon]
map = folium.Map(location=coordinates, tiles='OpenStreetMap',  zoom_start=12)
map 
#### save method of Map object will create a map
#### saved in Downloads
map.save("geopy_location.html")