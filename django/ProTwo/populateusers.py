import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User

from faker import Faker
fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fname1 = fake_name[0]
        lname1 = fake_name[1]
        email1 = fakegen.email()

        user = User.objects.get_or_create(fname = fname1, lname = lname1, email = email1)[0]

if __name__ == '__main__':
    print('Populating')
    populate(20)
    print("Complete!")