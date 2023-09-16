from django.urls import path
from . import views

app_name = 'blog'

# http://dominio.com.br/
urlpatterns = [
    path('', views.blog, name='home'),
    path('exemplo', views.exemplo, name='exemplo')
]
