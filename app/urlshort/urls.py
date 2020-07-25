from rest_framework import routers

from .views import UrlViewSet, MoveUrlsViewSet

router = routers.SimpleRouter()
router.register('urls', UrlViewSet)
router.register('moveurl', MoveUrlsViewSet)
urlpatterns = router.urls