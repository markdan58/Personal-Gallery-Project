from django.conf.urls import url
from . import views
import datetime as dt
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.displayphoto,name= 'displayphoto'), 
    url(r'^details/(\d+)',views.details,name= 'details'), 
    url(r'^search/',views.search_results,name= 'search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

