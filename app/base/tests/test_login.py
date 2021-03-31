import pytest
from django.urls import reverse

from app.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('login'))


def test_login_status_code(resp):
    assert resp.status_code == 200


def test_form_input_username(resp):
    assert_contains(resp, 'name="username"')


def test_form_input_password(resp):
    assert_contains(resp, 'name="password"')


def test_form_input_submit(resp):
    assert_contains(resp, 'value="Login"')


def test_reset_password_is_present(resp):
    link = reverse('password_reset')
    assert_contains(resp, f'href="{link}"')
