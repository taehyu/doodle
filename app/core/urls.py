from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

from app.urlshort.views import UrlShortViewSet, LinkViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'url', UrlShortViewSet)
router.register(r'link', LinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]