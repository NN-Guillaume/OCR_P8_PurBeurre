from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.index),

    #exemple OCR
    #url(r'^$', views.listing, name="listing"), #  "/store" will call the method "index" in "views.py"
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
    #url(r'^search/$', views.search, name="search"),

    path('index/', views.index ),
    path('connected/', views.connected),
    path('results/', views.results),
    path('aliment/', views.aliment),
    path('user_create/', views.user_create),
    path('user_account/', views.user_account),
]


