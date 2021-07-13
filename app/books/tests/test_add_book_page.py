import pytest
from django.urls import reverse

from app.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('books:add_book'))


def test_status_code(resp):
    assert resp.status_code == 302


def test_page_redirect(resp):
    assert resp.url.startswith(reverse('login'))


@pytest.fixture
def resp_logged_in(client_logged_in):
    return client_logged_in.get(reverse('books:add_book'))


def test_status_code_logged_in(resp_logged_in):
    assert resp_logged_in.status_code == 200


def test_page_title(resp_logged_in):
    title = 'Adicionar Livro | Estante'
    assert_contains(resp_logged_in, f'<title>{title}</title>')


def test_add_book_is_present_in_the_sidebar(resp_logged_in):
    content = '>Adicionar Livro</a>'
    assert_contains(resp_logged_in, content)


def test_add_book_link_is_present_in_the_sidebar(resp_logged_in):
    link = reverse('books:add_book')
    assert_contains(resp_logged_in, f'href="{link}"', count=1)
