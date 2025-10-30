"""
Author: Kaleb Mohr
Purpose: This script is the unit test for our lab web app.
We use pytest to test each function within that main script (app.py).
Date: 30 Oct 2025
"""

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Check if the homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Employee Lookup" in response.data

def test_check_title_found(client):
    """Verify if title lookup works."""
    response = client.post('/check_title', data={'name': 'Alice'})
    assert response.status_code == 200
    assert b"Network Engineer" in response.data

def test_check_title_not_found(client):
    """Verify unknown name returns 404 under the title search function."""
    response = client.post('/check_title', data={'name': 'Kaylie'})
    assert response.status_code == 404

def test_check_salary_found(client):
    """Verify salary lookup works."""
    response = client.post('/check_salary', data={'name': 'Charlie'})
    assert response.status_code == 200
    assert b"115000" in response.data

def test_check_salary_not_found(client):
    """Verify unknown name returns 404 under the salary search function."""
    response = client.post('/check_salary', data={'name': 'Minka'})
    assert response.status_code == 404


