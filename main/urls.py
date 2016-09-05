from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^addcomment/', views.add_comment, name='addcomment')
]