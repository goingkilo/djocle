from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader


from .models import Pic

def index0(request):
    return HttpResponse("Hello world!")

# Create your views here.

def index1(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def index2(request):
    mymembers = Pic.objects.all().values()
    output = ""
    for x in mymembers:
        output += x["name"]
    return HttpResponse(output)

def index(request):
    mymembers = Pic.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    print(request.POST)
    x = request.POST['name']
    y = request.POST['desc']
    member = Pic(name=x, desc=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Pic.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    pic = Pic.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mypic': pic,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['name']
    last = request.POST['desc']
    print('x',first,last,'x')
    pic = Pic.objects.get(id=id)
    pic.name = first
    pic.desc = last
    pic.save()
    return HttpResponseRedirect(reverse('index'))