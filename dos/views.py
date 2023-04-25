from django.shortcuts import render
import time
# from django.http import HttpResponse


def asunto(request):
    tiempo = time.ctime()
    valor = (4+4)
    texto = (f"la fecha es {tiempo} la suma es {valor}")
    return render(request, 'asunto.html', {"asunto": texto})
