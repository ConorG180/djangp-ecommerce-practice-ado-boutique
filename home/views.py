from django.shortcuts import render

def index(request):
    '''A view to return homepage'''
    return render(request, "home/index.html")
