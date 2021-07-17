import pytest
from django.urls import reverse

from app.books.models import BookModel
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


@pytest.mark.parametrize('content', [
    '<form method="post"',
    '<input type="text" name="title"',
    '<input type="text" name="author"',
    '<input type="number" name="published"',
    '<textarea name="description"',
    '<select name="read_status"',
    '<input type="submit" value="Salvar"',
])
def test_html_form_content(resp_logged_in, content):
    assert_contains(resp_logged_in, content)


@pytest.fixture
def post_form_data(client_logged_in):
    data = {
        'title': 'Book Title',
        'author': 'Book Author',
        'published': 2021,
        'description': 'Book Description',
        'read_status': 1,
    }
    return client_logged_in.post(reverse('books:add_book'), data)


def test_save_form_data(post_form_data):
    assert BookModel.objects.exists()


@pytest.fixture
def post_invalid_form_data(client_logged_in):
    return client_logged_in.post(reverse('books:add_book'), {})


def test_dont_save_invalid_form_data(post_invalid_form_data):
    assert not BookModel.objects.exists()
