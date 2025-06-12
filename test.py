import pytest
from main import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://cdn2.thecatapi.com/images/xyz.jpg'}]

    url = get_random_cat_image()
    assert url == 'https://cdn2.thecatapi.com/images/xyz.jpg'

def test_get_random_cat_image_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    url = get_random_cat_image()
    assert url is None


