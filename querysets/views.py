from django.shortcuts import render
import random
from .models import Restaurant
from faker import Faker

# Create your views here.
def generate_res(self):
    fake=Faker()
    for i in range(100):
        cuisines=["Chinese","Italian","Thai","Lebanese","Med"]
        r=Restaurant(
            name = fake.last_name(),
            city = fake.city(),
            cuisine_type = cuisines[random.randint(0,4)],
            rating = random.randint(1,5),
            is_open = getOpenState()
        )
        r.save()

def getOpenState():
    xd = random.randint(0,1)
    if xd==1:
        return True
    else:
        return False