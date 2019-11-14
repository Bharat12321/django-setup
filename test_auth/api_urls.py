# Third Party Stuff
from django.urls.converters import UUIDConverter
from rest_framework.routers import DefaultRouter

# Guardian Stuff
from first.routers import SingletonRouter
from first.api import AuthViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)
# Register all the django rest framework viewsets below.
default_router.register('auth', AuthViewSet, basename='auth')
# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = [
]
urlpatterns += default_router.urls + singleton_router.urls
