from ..models import Restaurant
from django.db import connection
from pprint import pprint

def run():
    # print(Restaurant.objects.count())

# filter()
    # print(Restaurant.objects.filter(cuisine_type='Thai'))

# get()
    print(Restaurant.objects.get(name='Page'))

# exists()
    print(Restaurant.objects.filter(name='Page').exists())
    print(Restaurant.objects.filter(name='xcvbn').exists())

    pprint(connection.queries)