from django.shortcuts import render
# from django.http import HttpResponse


#def index(request):
#    my_dict = {'insert_me': "Python Django webpage"}
#    return render(request, 'index.html', context=my_dict)

def index(request):
    title = ("Python webpage")
    listmenu = ['Inicio', 'Topic', 'Contacto', 'Localidad']

    return render(request, 'index.html', {"title": title, "listmenu": listmenu})
