import os
import django
import time
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country, City
url ="https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"

raw_data =pd.read_html(url)
time.sleep(3)  # for debug safety

data =raw_data[1]
countryId =list(data['countries']['id'])
countryName =list(data['countries']['name'])
countries =zip(countryId,countryName)

for c in countries:
    temp =Country(name =c[1],countryId =c[0])
    temp.save()

countries = Country.objects.all()
print(countries)
print('done')