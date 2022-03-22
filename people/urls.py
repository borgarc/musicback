from django.urls import path, include
from rest_framework.routers import DefaultRouter
from people.views import PersonView

router = DefaultRouter()
router.register(r'people', PersonView)

urlpatterns = [
    path('', include(router.urls)),
]