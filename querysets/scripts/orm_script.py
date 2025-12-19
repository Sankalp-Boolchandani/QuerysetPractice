from ..models import Restaurant
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower 

def run():
    # print(Restaurant.objects.count())

# filter()
    # print(Restaurant.objects.filter(cuisine_type='Thai'))

# get()
    # print(Restaurant.objects.get(name='Page'))

# exists()
    # print(Restaurant.objects.filter(name='Page').exists())
    # print(Restaurant.objects.filter(name='xcvbn').exists())

# filter with and - done using a (,) comma
    # print(Restaurant.objects.filter(name='Page', cuisine_type='Med'))
    # print(Restaurant.objects.filter(cuisine_type='Med', name__startswith='A'))

    # ch='Chinese'
    # it='Italian'
    # xd=[ch, it]
    # print(Restaurant.objects.filter(cuisine_type__in=xd))

# exclude()
    # print(Restaurant.objects.exclude(cuisine_type='Chinese'))
    # print(Restaurant.objects.exclude(cuisine_type__in=xd))

# lt/lte and gt/gte lookups
    # print(Restaurant.objects.filter(rating__gt=4))
    # print(Restaurant.objects.filter(rating__gte=4))
    # print(Restaurant.objects.filter(rating__lt=4))
    # print(Restaurant.objects.filter(rating__lte=4))

    # res=Restaurant.objects.filter(rating__range=(2,3))
    # print(res)

# order_by()
    print(Restaurant.objects.order_by('name'))
    print(Restaurant.objects.order_by('name').reversed())           # descending order
    print(Restaurant.objects.order_by('-name'))           # also descending order using minus(-)
    print(Restaurant.objects.order_by('name')[0])           # limit 1
    print(Restaurant.objects.order_by('name')[:5])           # limit 5
    print(Restaurant.objects.order_by('name')[2:5])           # limit 3 offset 2
    print(Restaurant.objects.order_by(Lower('name')))           # notes
    # pprint(connection.queries)