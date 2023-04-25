from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me': "My First website Python! 01"}
    return render(request, 'index.html', context=my_dict)


def index2(request):
    insert_me = ("My First website Python!")
    return render(request, 'index.html', {"insert_me": insert_me})
