import pytest

from pages.customer_login import CustomerLogin
from pages.triangle_page import TrianglePage


@pytest.fixture
def login_page(page):
    return CustomerLogin(page)

@pytest.fixture
def triangle_page(page):
    return TrianglePage(page)