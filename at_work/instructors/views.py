
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from instructors.models import Instructors


def instructors_list(request):
    instructors = Instructors.objects.all()
    return render(request, 'instructors.html', {'instructors_list': instructors})


def hello(request):
    context = {'var1': 'Hello python'}
    context['var2'] = {'some_str''Hello Chan'}
    context['var3'] = ['a', 'b', 'c']
    instructors = Instructors.objects.all()
    context['all_instructors'] = instructors
    return render(request, 'index.html', context)


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
