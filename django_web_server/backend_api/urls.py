from django.urls import path
from backend_api import views


urlpatterns = [
    path(route='', view=views.home, name=''),

    path(route='get_request/', view=views.get_request, name='get_request'),
    path(route='post_request/', view=views.post_request, name='post_request'),
]
