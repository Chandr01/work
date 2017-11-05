"""at_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def python_(request):
    return render(request, 'python.html')


def sum_num(request, a, b):
    c = int(a) + int(b)
    return HttpResponse('sum = ' + str(c))


urlpatterns = [
    url(r'^sum/(?P<a>\d+)&(?P<b>\d+)$', sum_num),
    url(r'^$', hello),
    url(r'^python/$', python_),
    url(r'^admin/', admin.site.urls),
]
