import os
import django
import time
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

url = "https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"

raw_data = pd.read_html(url)
time.sleep(3)  # for debug safety

data = raw_data[0]

from mysite.models import City, Country

cities = list()
for i in range(len(data)):
    temp = tuple(data['cities'].iloc[i])
    cities.append(temp)

for c in cities:
    cnt =Country.objects.get(countryId =c[2])
    temp = City(name=c[1], country=cnt, population=c[3])
    temp.save()

cities = Country.objects.all()
print(cities)
print('done')
