
import requests
import pandas as pd

# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type


# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""


def load_courts_near_postcode(postcode: str) -> list[dict]:
    """Given a postcode, loads the top 10 nearest courts to that postcode"""

    if not isinstance(postcode, str):
        raise TypeError('The postcode must be a string')

    url = f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}"

    response = requests.get(url)

    if response.status_code == 404:
        raise ConnectionError('Not Found!')

    if response.status_code == 500:
        raise ConnectionError('Server Error')

    if response.status_code == 200:
        data = response.json()

    return data
# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type


def load_people_from_csv(filename: str) -> list[dict]:
    """
    Loads the people and their details from the csv as a list of dictionaries
    Each person is a dictionary which has the keys: name, postcode and looking_for_court_type

    """

    people = pd.read_csv(filename)

    return people.to_dict('records')


def get_court_for_person(person: dict) -> dict:

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

    people_with_courts = []

    for person in people:
        person = get_court_for_person(person)
        people_with_courts.append(person)

    final_dataframe = pd.DataFrame(people_with_courts)

    return final_dataframe


if __name__ == "__main__":
    # [TODO]: write your answer here

    people = load_people_from_csv("people.csv")

    people_with_courts = add_courts_for_all_people(people)

    print(people_with_courts)
