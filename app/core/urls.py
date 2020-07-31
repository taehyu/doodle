from django.conf.urls import url

from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

# from app.urlshort.views import UrlShortViewSet, LinkViewSet
# from rest_framework.routers import SimpleRouter
#
#
# from django.urls import path, include
# from rest_framework import routers
# from short.views import ShortViewSet
# from urlshort.views import UrlViewSet
#
# router = routers.SimpleRouter(trailing_slash=False)
# # router.register(r'url', UrlShortViewSet)
# # router.register(r'link', LinkViewSet)
# router.register(r'urls', UrlViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
from rest_framework.routers import SimpleRouter

from short.views import ShortViewSet
from users.views import UsersViewSet, DoodleViewSet

router = SimpleRouter()
router.register(r'short', ShortViewSet)
router.register(r'users', UsersViewSet)
router.register(r'doodle', DoodleViewSet)
urlpatterns = router.urls
