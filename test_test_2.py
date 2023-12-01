"""Testing the functions in test_2.py"""

import pytest
from unittest.mock import patch

from test_2 import load_courts_near_postcode, load_people_from_csv, get_court_for_person, add_courts_for_all_people

BASE_URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode="


def test_load_courts_near_postcode(requests_mock):

    postcode = 'LE23WL'
    requests_mock.get(f"{BASE_URL}{postcode}",
                      status_code=200, json=[{}])

    load_courts_near_postcode(postcode)

    assert requests_mock.called
    assert requests_mock.call_count == 1
    assert requests_mock.last_request.method == "GET"


def test_load_courts_near_postcode_error_404(requests_mock):

    postcode = 'LE23WL'
    requests_mock.get(f"{BASE_URL}{postcode}",
                      status_code=404, json=[{}])

    with pytest.raises(ConnectionError):
        load_courts_near_postcode(postcode)


def test_load_courts_near_postcode_error_500(requests_mock):

    postcode = 'LE23WL'
    requests_mock.get(f"{BASE_URL}{postcode}",
                      status_code=500, json=[{}])

    with pytest.raises(ConnectionError):
        load_courts_near_postcode(postcode)


def test_load_courts_near_postcode_invalid_type():
    postcode = 5647

    with pytest.raises(TypeError):
        load_courts_near_postcode(postcode)


def test_load_people_from_csv_invalid_type():
    filename = 21

    with pytest.raises(TypeError):
        load_people_from_csv(filename)


def test_get_court_for_person_invalid_type():
    person = 'ishika madhav'

    with pytest.raises(TypeError):
        get_court_for_person(person)


def test_get_court_for_person_working():

    person = {'person_name': 'ishika', 'home_postcode': 'LE23WL',
              'looking_for_court_type': "Tribunal"}

    result = get_court_for_person(person)

    assert isinstance(result, dict) == True
    assert len(result.keys()) == 6


def test_add_courts_for_all_people_invalid_type():
    people = {'name': 'ishika'}

    with pytest.raises(TypeError):
        add_courts_for_all_people(people)
