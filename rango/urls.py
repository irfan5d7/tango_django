from django .urls import path
from django.conf import settings

from rango import views
from rango.Views import *
from rango.views import *
from django.conf.urls import include, url
app_name = 'rango'
from rango.Views import *
urlpatterns = [
    url('index/',index,name= 'index'),
    url(r'rango/',index,name='index'),
    url(r'about/$', about, name='about'),
    url('add_category/',add_category,name='add_category'),
    url(r'^suggest/$',suggest_category, name='suggest_category'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/add_page/$', add_page, name='add_page'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/$',show_category, name='show_category'),
    url(r'^register/$',register,name = 'register'),
    url(r'^login/$',user_login, name='login'),
    url(r'^restricted/',restricted,name='restricted'),
    url(r'^logout/$',user_logout,name ='logout'),
    url(r'^search_bing/', search_bing, name='search_bing'),
    url(r'goto/$',track_url,name = 'goto'),
    url(r'^register_profile/$',register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$',profile, name='profile'),
    url(r'^like_category/$',like_category,name='like_category'),
]