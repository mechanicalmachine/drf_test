from rest_framework.routers import DefaultRouter

from .views import MetricsViewSet


router = DefaultRouter()
router.register(r'metrics', MetricsViewSet, basename='metrics')
urlpatterns = router.urls
