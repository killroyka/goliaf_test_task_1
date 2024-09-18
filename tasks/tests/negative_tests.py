import json

import pytest
from django.urls import reverse

from tasks.models import Task


@pytest.mark.django_db
def test_post_required_fields_task(client):
    post_url = reverse('task-list')
    response = client.post(post_url, data={"description": "test"})
    assert response.status_code == 400


@pytest.mark.django_db
def test_post_max_length_task(client):
    post_url = reverse('task-list')
    response = client.post(post_url, data={"title": "a" * 101})
    assert response.status_code == 400


@pytest.mark.django_db
def test_post_completed_type_task(client):
    post_url = reverse('task-list')
    response = client.post(post_url, data={"title": "test", "completed": 100})
    assert response.status_code == 400


@pytest.mark.django_db
def test_put_not_exist_task(client):
    url = reverse('task-detail', kwargs={'pk': -1})
    response = client.put(url, data=json.dumps({"title": "test passed", "completed": True, "description": "passed"}),
                          content_type="application/json")
    assert response.status_code == 404


@pytest.mark.django_db
def test_put_required_fields_task(client):
    task = Task.objects.create(title="test_put_1")
    task.save()
    url = reverse('task-detail', kwargs={'pk': task.pk})
    response = client.put(url, data=json.dumps({"completed": True, "description": "passed"}),
                          content_type="application/json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_put_completed_type_task(client):
    task = Task.objects.create(title="test_put_1")
    task.save()
    url = reverse('task-detail', kwargs={'pk': task.pk})
    response = client.put(url, data=json.dumps({"completed": 100, "description": "passed"}),
                          content_type="application/json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_put_max_length_task(client):
    task = Task.objects.create(title="test_put_1")
    task.save()
    url = reverse('task-detail', kwargs={'pk': task.pk})
    response = client.put(url, data=json.dumps({"title": "a" * 101, "description": "passed"}),
                          content_type="application/json")
    assert response.status_code == 400


@pytest.mark.django_db
def test_delete_not_exist_task(client):
    url = reverse('task-detail', kwargs={'pk': -1})
    response = client.delete(url, content_type="application/json")
    assert response.status_code == 404
