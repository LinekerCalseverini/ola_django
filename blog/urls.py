from django.urls import path
from blog import views

app_name = 'blog'

# blog/
# Django URLs:
# https://docs.djangoproject.com/en/4.2/topics/http/urls/
urlpatterns = [
    path('', views.blog, name='home'),
    path('<int:post_id>/', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo')
]
