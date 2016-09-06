from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^add_comment/', views.add_comment, name='add_comment'),
    url(r'edit_comment/', views.edit_comment, name='edit_comment'),
    url(r'^rm_comment/', views.rm_comment, name='rm_comment'),
]