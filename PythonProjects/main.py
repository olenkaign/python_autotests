import requests
import json

token = 'b6a8849fef25dd272399da0e43f22083'

response = requests.post('https://pokemonbattle.me:5000/pokemons', json= {
    "name": "Мустанг",
    "photo": "https://dolnikov.ru/pokemons/05.png"
}, headers= {'Content-Type': 'application/json', 'trainer_token' : token})

print(response.text)

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', json= {
    "pokemon_id": '4651',
    "name": "Мусташка",
    "photo": "https://dolnikov.ru/pokemons/05.png"
}, headers= {'Content-Type': 'application/json', 'trainer_token' : token} )

print(response_change.text)

response_pokeball = requests.put('https://pokemonbattle.me:5000/trainers/add_pokeball', json= {
    "pokemon_id": '4651', 
}, headers= {'Content-Type': 'application/json', 'trainer_token' : token} )

print(response_change.text)




