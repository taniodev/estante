import pytest
from django.urls import reverse

from app.django_assertions import assert_contains


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


def test_page_title(resp_logged_in):
    title = 'Lendo Agora | Estante'
    assert_contains(resp_logged_in, f'<title>{title}</title>')


def test_reading_now_is_present_in_the_sidebar(resp_logged_in):
    content = '>Lendo Agora</a>'
    assert_contains(resp_logged_in, content)


def test_reading_now_link_is_present_in_the_sidebar(resp_logged_in):
    link = reverse('books:reading_now')
    # This link is present in the header and in the sidebar
    assert_contains(resp_logged_in, f'href="{link}"', count=2)
