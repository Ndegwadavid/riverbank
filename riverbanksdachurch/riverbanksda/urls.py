from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import download_book, upload, home, resources, bibleverse, upload_file
urlpatterns = [
    path('', views.index, name='index'),
   path('home/', views.home, name='home'),
   path('resources/', views.resources, name='resources'),
   path('bibleverse/', views.bibleverse, name='bibleverse'),
   path('download/<int:book_id>/', download_book, name='download_book'),
   path('list/', upload_file, name='list'),
   path('login/', views.login, name='login'),
   path('planets/', views.planets, name='planets'),
   path('upload/', views.upload, name='upload'),
   path('prayerrequests/', views.prayerrequests, name='prayerrequests'),
   path('sermons/', views.sermons, name='sermons'),
   path('spiritofprophecy/', views.spiritofprophecy, name='spiritofprophecy'),
   path('trinity/', views.trinity, name='trinity'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)