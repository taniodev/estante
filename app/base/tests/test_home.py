import pytest
from django.urls import reverse

from app.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('base:home'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_home_link_is_present(resp):
    # In the header of all pages
    link = reverse('base:home')
    assert_contains(resp, f'href="{link}"')


def test_login_link_is_present(resp):
    # In the header of all pages
    link = reverse('login')
    assert_contains(resp, f'href="{link}"')


def test_logout_link_is_not_present(resp):
    # Appears only when the user is logged in
    link = reverse('logout')
    assert_not_contains(resp, f'href="{link}"')


@pytest.fixture
def resp_logged_in(client_logged_in):
    return client_logged_in.get(reverse('base:home'))


def test_login_link_is_not_present(resp_logged_in):
    link = reverse('login')
    assert_not_contains(resp_logged_in, f'href="{link}"')


def test_logout_link_is_present(resp_logged_in):
    link = reverse('logout')
    assert_contains(resp_logged_in, f'href="{link}"')
