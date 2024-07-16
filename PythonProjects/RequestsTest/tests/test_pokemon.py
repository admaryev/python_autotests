import requests
import pytest

URL = 'https://api.pokemonbattle.ru/'
TOKEN = 'de60a400c9838d3003dacb71e98106fe'
HEADER = {"Content-Type" : "application/json",
          "trainer_token" : TOKEN}
trainer_id = '4121'


def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers')
    assert response.status_code == 200

def test_trainer():
    response_trainer = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : trainer_id})
    assert response_trainer.json()["data"][0]["trainer_name"] == "Котофей"

    