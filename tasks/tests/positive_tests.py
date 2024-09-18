import json

import pytest
from django.urls import reverse

from tasks.models import Task
from tasks.serializers import TaskSerializer


@pytest.mark.django_db
def test_delete_exist_task(client):
    task = Task.objects.create(title="test_delete_1")
    task.save()
    url = reverse('task-detail', kwargs={'pk': task.pk})
    response = client.delete(url, content_type="application/json")
    assert response.status_code == 204
    assert Task.objects.filter(id=task.id).exists() is False


@pytest.mark.django_db
def test_put_exist_task(client):
    task = Task.objects.create(title="test_put_1")
    task.save()
    url = reverse('task-detail', kwargs={'pk': task.pk})
    response = client.put(url, data=json.dumps({"title": "test passed", "completed": True, "description": "passed"}),
                          content_type="application/json")
    expected_data = TaskSerializer(Task.objects.get(id=task.id)).data
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_list_articles(client):
    for x in range(10):
        task = Task.objects.create(title="test_list_" + str(x))
        task.save()
    url = reverse('task-list')
    response = client.get(url)

    articles = Task.objects.all()
    expected_data = TaskSerializer(articles, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_post_task(client):
    post_url = reverse('task-list')
    response = client.post(post_url, data={"title": "test1"})
    expected_data = TaskSerializer(Task.objects.get(pk=response.data['id'])).data
    assert response.status_code == 201
    assert response.data == expected_data
