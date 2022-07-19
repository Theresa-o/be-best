from django.urls import path, include
from rest_framework import routers
from .views import ListViewSet, ListItemViewSet

router = routers.DefaultRouter()
router.register(r'', ListViewSet)
router.register(r'', ListItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
