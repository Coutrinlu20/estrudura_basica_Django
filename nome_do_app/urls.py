from django.urls import path, include
from nome_do_app.views import home

urlpatterns = [
    path('', home, name='home'),
]