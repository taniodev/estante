import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('books:reading_now'))


def test_status_code(resp):
    assert resp.status_code == 302


def test_page_redirect(resp):
    assert resp.url.startswith(reverse('login'))


@pytest.fixture
def resp_logged_in(client_logged_in):
    return client_logged_in.get(reverse('books:reading_now'))


def test_status_code_logged_in(resp_logged_in):
    assert resp_logged_in.status_code == 200
