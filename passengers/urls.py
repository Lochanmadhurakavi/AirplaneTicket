from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.createPassenger, name='create'),
    path('create/<str:pk>', views.viewPassenger, name="view"),
    path('create/<str:pk>/update', views.updatePassenger, name='update'),
    path('create/<str:pk>/delete', views.deletePasseger, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)