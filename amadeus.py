import requests
import logging
import sys

from apiwrapper import APIWrapper

API_URL = 'https://api.sandbox.amadeus.com/v1.2'


def configure_logger(log_level=logging.WARN):
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    try:
        sa = logging.StreamHandler(stream=sys.stdout)
    except TypeError:
        sa = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
    sa.setFormatter(formatter)
    logger.addHandler(sa)
    return logger

log = configure_logger()
STRICT, GRACEFUL, IGNORE = 'strict', 'graceful', 'ignore'

class Transport(APIWrapper):

	def __init__(self, api_key, api_url=API_URL):
	    if not api_key:
	        log.warning("API Key is not set.")
	    self.api_key = '0rVN20m0UoLP9Ur9dyKg8MindOEAEtOk'
	    self.api_url = api_url

def make_request(self, service_url, method='get', headers=None, data=None, callback=None, errors=STRICT, **params):
    params.update({'apikey': self.api_key})
    request = getattr(requests, method.lower())
    r = request(service_url, headers=headers, data=data, params=params)
    return r.json()


def get_location(self, code='BKK'):
    loc_key = "loc-{code}".format(code=code)
    path = "location/{code}".format(code=code)
    service_url = "{url}/{path}".format(url=self.api_url, path=path)
    loc_data = self.make_request(service_url)

    return loc_data

def search_airport(self, **params):
    service_url = "{url}/{path}".format(
        url=self.api_url, path='search-airport')
    return self.make_request(service_url, **params)

def search_circle(self, **params):
    service_url = "{url}/{path}".format(
        url=self.api_url, path='search-circle')
    return self.make_request(service_url, **params)

def extensive_search(self, **params):
    service_url = "{url}/{path}".format(
        url=self.api_url, path='extensive-search')
    return self.make_request(service_url, **params)


class Flights(Transport):

	def __init__(self, api_key, api_url=API_URL):
	    self.api_url = "{api_url}/flights".format(api_url=api_url)
	    self.api_key = '0rVN20m0UoLP9Ur9dyKg8MindOEAEtOk'

def low_fare_search(self, **params):
    service_url = "{url}/{path}".format(
        url=self.api_url, path='low-fare-search')
    return self.make_request(service_url, **params)


class Hotels(Transport):

	def __init__(self, api_key, api_url=API_URL):
	    super(Hotels, self).__init__(api_key=api_key, api_url=api_url)
	    self.api_url = "{api_url}/hotels".format(api_url=api_url)

def search_property_code(self, **params):
    service_url = "{url}/{path}".format(
        url=self.api_url, path=params['property_code'])
    return self.make_request(service_url, **params)



class TravelIntelligence(Transport):

	def __init__(self, api_key, api_url=API_URL):
	    super(TravelIntelligence, self).__init__(
	        api_key='0rVN20m0UoLP9Ur9dyKg8MindOEAEtOk', api_url=api_url)
	    self.api_url = "{api_url}/travel-intelligence".format(api_url=api_url)

def top_destinations(self, **params):
    service_url = "{url}/{path}".format(
        url=self.api_url, path="top-destinations")
    return self.make_request(service_url, **params)