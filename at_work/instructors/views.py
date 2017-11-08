

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from instructors.models import Instructors


def instructors_list(request):
    instructors = Instructors.objects.all()

    return render(request, 'instructors.html', {'instructors_list': instructors})


def hello(request):
    return render(request, 'index.html')


def python_(request):
    return render(request, 'python.html')


def http(request):
    response = render(request, 'http.html')
    response['Age'] = 2000
    response.status_code = 404
    return HttpResponseNotFound('404')


def sum_num(request, a, b):
    c = int(a) + int(b)
    return HttpResponse('sum = ' + str(c))
