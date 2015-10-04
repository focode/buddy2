import requests
import googlemaps


def getAddress(latitude,longitude):
    # grab some lat/long coords from wherever. For this example,
    # I just opened a javascript console in the browser and ran:
    #
    # navigator.geolocation.getCurrentPosition(function(p) {
    #   console.log(p);
    # })
    #


    # Did the geocoding request comes from a device with a
    # location sensor? Must be either true or false.
    sensor = 'false'

    # Hit Google's reverse geocoder directly
    # NOTE: I *think* their terms state that you're supposed to
    # use google maps if you use their api for anything.
    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=latitude,
        lon=longitude,
        sen=sensor
    )
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    print response.content
    gmaps = googlemaps.Client(key='AIzaSyAbd96ALSLp73pg8w9MH3sziZnZVv64oCM')
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))


    googleaddress = 'someval'
    for element in reverse_geocode_result:
        print element['formatted_address']
        googleaddress = element['formatted_address']
        break


    return googleaddress