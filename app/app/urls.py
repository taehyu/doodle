"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.authtoken import views
# from rest_framework.routers import SimpleRouter
#
# from urlshort.views import UrlShortViewSet, RedirecturlViewSet
#
# router = SimpleRouter()
# # router.register(r'users', UserViewSet, basename='users')
# router.register(r'urlshort', UrlShortViewSet, basename='shortener')
# router.register(r'happy', RedirecturlViewSet, basename='redirect')
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url('', include(router.urls)),
# ]

from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from rest_framework.routers import SimpleRouter


def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('sentry-debug/', trigger_error),
]

# router = routers.SimpleRouter()
# router.register(r'urls', UrlViewSet)
# urlpatterns += router.urls


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

