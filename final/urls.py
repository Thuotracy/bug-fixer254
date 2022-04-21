from django.urls import path
from final.views import *

urlpatterns=[
  path('register/', register, name='register'),
  path('', login_view, name='login'),
  path('logout/', logout_view, name='logout'),
  path('home', home, name='home'),
  path('search/', search_site, name='search_site'),
  path('complaint/', complaint, name='complaint'),
  path('progress/', progress, name='progress'),
]