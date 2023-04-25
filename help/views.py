from django.shortcuts import render


def help(request):
    help = ("Help this is the place")
    return render(request, 'help.html', {"help": help})
