"""Proyecto_Uno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
# from django.contrib import admin
# from django.conf.urls import include
# from help.views import help


from uno.views import index
# from dos.views import asunto
from tres.views import tres


urlpatterns = [
    path('', index, name='index'),
    path('asunto/', include('dos.urls')),  # metodo con URL EN APP
    # path('admin/', admin.site.urls),
    path('tres', tres, name='tres'), # Metodo SIN URL APP
    path('help/', include('help.urls')),   # metodo con URL EN APP
]
