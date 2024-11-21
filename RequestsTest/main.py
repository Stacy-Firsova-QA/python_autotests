import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TRAINER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create_pokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}


response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.text)

pokemon_id = response_create_pokemon.json()['id']
body_change_name = {
    "pokemon_id": pokemon_id,
    "name": "New Name"
}

response_change_name = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
