import pytest
from model_bakery import baker


@pytest.fixture
def fake_user_logged_in(db, django_user_model):
    user = baker.make(django_user_model)
    return user


@pytest.fixture
def client_logged_in(client, fake_user_logged_in):
    client.force_login(fake_user_logged_in)
    return client
