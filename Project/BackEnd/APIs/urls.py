from django.urls import path
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import views



router = DefaultRouter()
router.include_format_suffixes = False
# router.register('', views., basename='')


urlpatterns = [
    path('', include(router.urls)),
    path('longterm/', views.LongTermViewSet.as_view(), name='LongTerm'),
    path('shortterm/', views.ShortTermViewSet.as_view(), name='ShortTerm'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)