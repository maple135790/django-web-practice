from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from  django.contrib.auth import logout
import numpy as np
import logging
from plotly.offline import plot
import plotly.graph_objs as go
from mysite.models import City, Country, Post
import random

logger = logging.getLogger("mylogger")

def index(request):
    name ='kenneth'
    lottery = [random.randint(1, 43) for _ in range(5)]
    special = random.randint(1, 43)
    x = np.linspace(-6*np.pi, 6*np.pi, 360)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plot_div = plot([
        go.Scatter(x=x, y=y1,
                   mode='lines', name='SIN',
                   opacity=0.8, marker_color='green'),

        go.Scatter(x=x, y=y2,
                   mode='lines', name='COS',
                   opacity=0.8, marker_color='blue')
    ],
        output_type='div')
    return render(request, "index.html", locals())


def news(request):
    posts = Post.objects.all()
    return render(request, 'news.html', locals())


def show(request, id):
    try:
        post = Post.objects.get(id=id)  # find one record
    except:
        return redirect('/news/')
    return render(request, 'show.html', locals())




def rank(request):
    if request.method == 'POST':
        cid = request.POST["countryId"]
        try:
            logger.info(cid)
            selectedCountry = Country.objects.get(id=cid)
            logger.info(selectedCountry)
            # print(selectedCountry)
            cities = City.objects.filter(country=selectedCountry)
        except Exception as e:
            logger.info(e)
            return redirect('/news/')
    else:
        cities = City.objects.all()
    countries = Country.objects.all()
    return render(request, 'rank.html', locals())

@login_required(login_url='/admin/login/')
def chart(request):
    if request.method == 'POST':
        cid = request.POST["id"]
        logger.info(cid)
        if cid.strip()=="999":
            return redirect("/chart/")
        try:
            country = Country.objects.get(id=cid)
        except:
            return redirect("/chart/")
        cities = City.objects.filter(country=country)
    else:
        cities = City.objects.all()
    countries = Country.objects.all()
    names = [city.name for city in cities]
    population = [city.population for city in cities]
    return render(request, "chart.html", locals())

def mylogout(request):
    logout(request)
    return redirect('/')
