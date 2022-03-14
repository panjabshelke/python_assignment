import django
import pytest
from rest_framework.test import APIClient
from unittest.mock import patch
import factory
from faker import Factory
import random

pytestmark = pytest.mark.django_db

django.setup()

from api import models

faker = Factory.create()


class RouterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.RouterDetails

    loop_back = random.randint(0, 19999)
    sap_id = random.randint(0, 19999)
    host_name = random.randint(0, 19999)
    mac_address = random.randint(0, 19999)


@pytest.fixture
def single_router(*args, **kwargs):
    return RouterFactory(*args, **kwargs)


@pytest.fixture
def client():
    return APIClient()


def test_roter_get_unauthorized(client):
    response = client.get('/api/v1/router-details')
    assert response.status_code == 401


def test_router_get_authorized(client, single_router):
    with patch("rest_framework.permissions.IsAuthenticated.has_permission") as p:
        # test GET method
        get_response = client.get('/api/v1/router-details')
        assert get_response.status_code == 200

        # test Delete Method
        del_response = client.delete(f'/api/v1/router-details/{single_router.loop_back}')
        assert del_response.status_code == 204
