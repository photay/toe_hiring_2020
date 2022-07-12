from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'dogquestions', views.DogQuestionViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
