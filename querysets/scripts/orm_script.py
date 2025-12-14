from ..models import Restaurant
from django.db import connection
from pprint import pprint

def run():
    # print(Restaurant.objects.count())

# filter()
    print(Restaurant.objects.filter(cuisine_type='Thai'))
    pprint(connection.queries)