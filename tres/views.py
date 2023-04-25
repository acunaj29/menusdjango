from django.shortcuts import render


def tres(request):
    webpage = ("THIS IS THE WEBPAGE 03")
    return render(request, 'tres.html', {"tres": webpage})
