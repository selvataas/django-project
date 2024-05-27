from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return render(request, 'index.html')

def hakkimizda(request):
    return HttpResponse('hakkımızda sayfası')

def iletisim(request):
    return HttpResponse('iletişim sayfası')