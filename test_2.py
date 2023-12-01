"""Script that analyses the dataset of people and their desired court types, determining the distance
to the nearest court of the specific court type specified for each person """

import requests
import pandas as pd

BASE_URL = "https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode="
NOT_FOUND = 404
SERVER_ERROR = 500
SUCCESS = 200


def load_courts_near_postcode(postcode: str) -> list[dict]:
    """
    Given a postcode, loads the top 10 nearest courts to that postcode
    as a list of dictionaries
    """

    if not isinstance(postcode, str):
        raise TypeError('The postcode must be a string')

    url = f"{BASE_URL}{postcode}"

    response = requests.get(url, timeout=10)

    if response.status_code == NOT_FOUND:
        raise ConnectionError('Not Found!')

    if response.status_code == SERVER_ERROR:
        raise ConnectionError('Server Error')

    if response.status_code == SUCCESS:
        data = response.json()

    return data


def load_people_from_csv(filename: str) -> list[dict]:
    """
    Loads the people and their details from the csv as a list of dictionaries
    Each person is a dictionary which has the keys: name, postcode and looking_for_court_type

    """

    if not isinstance(filename, str):
        raise TypeError('The filename needs to be a string')

    people_data = pd.read_csv(filename)

    return people_data.to_dict('records')


def get_court_for_person(person: dict) -> dict:
    """
    Given a person, as a dictionary, using the court type the person has requested
    will find the closest court of that type and add it's details to the dictionary
     e.g court name, dx number and distance from postcode """

    if not isinstance(person, dict):
        raise TypeError('Person needs to be a dictionary')

    postcode = person['home_postcode']
    court_type_wanted = person['looking_for_court_type']

    court_data = load_courts_near_postcode(postcode)

    for court in court_data:
        try:
            court_type = court['types'][0]
        except:
            court_type = None

        if court_type == court_type_wanted:
            person['type'] = person.pop('looking_for_court_type')
            person['court_name'] = court['name']
            person['court_dx_number'] = court['dx_number']
            person['distance'] = court['distance']

            break

    return person


def add_courts_for_all_people(people: list[dict]) -> pd.DataFrame:
    """
    Given people as a list of dictionaries
    will add the desired court information for each person
    and then return a pandas Dataframe with columns:
    person name, home postcode, type, court name, dx number and distance
    """

    if not isinstance(people, list):
        raise TypeError('People needs to be a list of dictionaries')

    people_with_courts = []

    for person in people:
        person = get_court_for_person(person)
        people_with_courts.append(person)

    final_dataframe = pd.DataFrame(people_with_courts)

    return final_dataframe


if __name__ == "__main__":

    people = load_people_from_csv("people.csv")

    people_and_court = add_courts_for_all_people(people)

    print(people_and_court)
