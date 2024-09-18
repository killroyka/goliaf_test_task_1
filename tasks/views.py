from rest_framework import viewsets, mixins

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
                mixins.UpdateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
