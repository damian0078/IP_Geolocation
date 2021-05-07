import requests
import json

#API to check my public ip address
ip = requests.get("https://api.ipify.org").text

#Lists
us_east = ["US", "BR"]
eu_central = ["PL", "DE", "IL", "GB"]

#IP Geolocation API
response = requests.get("http://ipwhois.app/json/"+ ip +"?objects=country,city,country_code,latitude,longitude")
data = response.json()

#Printing data in the right format from API
print("IP Address :  {0}".format(ip))
print("Country Code: {0}".format((data)["country_code"]))
print("Country: {0}".format((data)["country"]))
print("City: {0}".format((data)["city"]))
print("Latitude: {0}".format((data)["latitude"]))
print("Longitude: {0}".format((data)["longitude"]))

#Checking if the mapping is supported and printing nearest region.
if (data)["country_code"] in us_east:
    print("Nearest Region: us-east-2 (Ohio)")
elif (data)["country_code"] in eu_central:
    print("Nearest Region: eu-central-1 (Frankfurt)")
else:
    print("Country is not supported in the mapping")