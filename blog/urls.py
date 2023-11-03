from django.urls import path
from .import views

urlpatterns=[
path('',views.list_view ),
path('sport.html',views.sport),
path('political.html',views.political),
path('economy.html',views.economy),
path('social.html',views.social),
path('art.html',views.art),
path('cultur.html',views.cultur),
path('<int:year>/<int:month>/<int:day>/<str:slug>/',views.detail_view)
 ]