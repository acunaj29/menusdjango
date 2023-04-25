from django.urls import path
from dos.views import asunto


urlpatterns = [
    path('', asunto, name='asunto')
]
