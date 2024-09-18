from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TasksView

router = DefaultRouter()
router.register(r'', TasksView, basename='task')
urlpatterns = [] + router.urls
print(urlpatterns)