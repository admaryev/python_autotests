import requests

URL = 'https://api.pokemonbattle.ru/'
TOKEN = 'de60a400c9838d3003dacb71e98106fe'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}


pokemons_creat = {
    "name": "Pokemonchik",
    "photo_id": 2
}




respons_creat = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = pokemons_creat)
print(respons_creat.json())

pokemons_id = respons_creat.json()['id']
pokemons_change = {
    "pokemon_id": pokemons_id,
    "name": "Rock",
    "photo_id": 4
}

respones_change = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = pokemons_change)
print(respones_change.json())

response_add = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = {'pokemon_id': pokemons_id })
print(response_add.json())

