from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('',views.list_view ),
path('sport.html',views.sport),
path('political.html',views.political),
path('economy.html',views.economy),
path('social.html',views.social),
path('art.html',views.art),
path('cultur.html',views.cultur),
path('<int:year>/<int:month>/<int:day>/<str:slug>/',views.detail_view),
 ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)