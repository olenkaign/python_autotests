import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_fragment_of_response():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params= {'trainer_id' : '2003'})
    assert response.json()['trainer_name'] == 'Ольга Игнатьева'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Ольга Игнатьева'), ('city', 'Санкт-Петербург')])

def test_parametr(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params= {'trainer_id' : '2003'})
    assert response.json()[key] == value