import json

from django.shortcuts import render
from django.http import HttpResponse
from hotel_api.models import Booking
from rest_framework import viewsets, generics
from hotel_api.serializers import BookingSerializer
from django.views.decorators.http import require_http_methods
from requests import request

CATEGORY_ID = "4bf58dd8d48988d1fa931735"
VERSION = "20200101" #YYYYMMDD

longitude = "6.5068271"
latitude = "3.3783093"
CLIENT_SECRET = "MN0XTRAKQNFMKNUVVDG3KOJ2GVHKYK1VFDMF0DRSH0SS30SQ"
CLIENT_ID = "K4S114CZZPVH0IYPWJHT4TASX2GYP4HM2ET1PLZM2ACLCO5Q"

def fetch_hotels(longitude, latitude):
    ''' fet from api: for hotels '''

    # the api url
    url = f"https://api.foursquare.com/v2/venues/search?ll={longitude},{latitude}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&v={VERSION}&categoryId={CATEGORY_ID}"
    
    try:
        response = request("GET", url)
    
    except Exception as e:
        print(e)
        return None

    return json.loads(response.text.encode('utf8'))

def prepare_response(response):
    ''' prepares a dictionary as an HTTP response '''
    return HttpResponse(json.dumps(response))

@require_http_methods(['GET'])
def property_bookings(request, property_id=None):
    ''' get all bookings for property_id '''
    # get response
    response = {status:False}

    if property_id is None or (type(property_id) == str and not property_id.isalnum()):
        # respond
        return prepare_response(response)
    
    # write other code here
    # call places/hotels api ....

    # respond
    return prepare_response(response)

@require_http_methods(['GET'])
def properties(request, lat=None, long=None):
    ''' get all properties at closest hotels to the lat and long provided '''
    long = "6.5068271"
    lat = "3.3783093"

    def isfloat(text):
        ''' for cheking if a string is float '''
        return text.replace('.', '', 1).isdigit()

    response = {'status':False, 'data':[]}

    # get response
    if lat is None or long is None or not isfloat(lat) or not isfloat(long):
        # respond
        return prepare_response(response)

    # write other code here
    hotels = fetch_hotels(long, lat)
    
    # check if the api fetch for null
    if hotels is None:
        # respond
        return prepare_response(response)

    # get the response details
    resp = hotels.get("response", {})
    venues = resp.get('venues', [])

    # extract necessary hotels details
    for hotel_info in venues:
        hotel_details = {}

        hotel_details['id'] = hotel_info.get('id', -1)
        hotel_details['name'] = hotel_info.get('name', "")
        hotel_details['distance'] = hotel_info.get('location', {}).get('distance', -1)
        hotel_details['address'] = ', '.join(hotel_info.get('location', {}).get('formattedAddress', []))
    
        # dict details to hotel list
        response['data'].append(hotel_details)
    
    # respond
    return prepare_response(response)

# Create your views here.
class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-timestamp')
    serializer_class = BookingSerializer
