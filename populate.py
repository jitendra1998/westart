import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'westart.settings')


import django
django.setup()

import random

from dashboard.models import UserDetails, StartUps, Menudetails
from faker import Faker
from random import randint

fakegen = Faker()
# topics = ['Serach','Social','Marketplace','News','Games']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        first_name = fake_name[0]
        last_name = fake_name[1]
        fake_email = fakegen.email()

        user = UserDetails.objects.get_or_create(username= "_".join(fake_name).lower(),password=first_name,email=fake_email,type=1)[0]
        user.save()

        for i in range(3):
            name = fakegen.company()
            des = fakegen.text(max_nb_chars=200, ext_word_list=None)
            webpg = StartUps.objects.get_or_create(start_up_username=user,start_up_name=name,start_up_description=des)[0]
            webpg.save()

            for i in range(3):
                item = fakegen.word()
                no = randint(50,100)
                ebpg = Menudetails.objects.get_or_create(Menu_start_up_name=webpg.start_up_name,Menu_start_up_item=item,Menu_start_up_item_price=no)[0]

        # top = add_topic()
        # fake_url = fakegen.url()
        # fake_date = fakegen.date()
        # fake_name = fakegen.company()
        #
        # webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        #
        # acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populateing ")

    populate(5)
    print("comple")
