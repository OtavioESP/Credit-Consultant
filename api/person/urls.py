from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from person.views import PersonView

router = routers.SimpleRouter(trailing_slash=False)
router.register('persons', PersonView,
                basename='persons')

urlpatterns = [
    path('', include(router.urls)),
] + router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
