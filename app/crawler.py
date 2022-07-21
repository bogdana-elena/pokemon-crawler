import math

import requests

from app.models import Generation, Pokemon, Ability

POKE_API_URL = " https://pokeapi.co/api/v2/pokemon"


# session = requests.Session()


class PokemonCrawler:
    def crawl(self):
        # find urls to go through
        response = requests.get(POKE_API_URL, params={'limit': 100000, 'offset': 0}).json()
        pokemon_count = response['count']

        for pokemon_index in range(5):    # range(pokemon_count + 1):
            pokemon_url = response['results'][pokemon_index]['url']
            pokemon_response = requests.get(pokemon_url).json()
            # save to the database - could create a PokemonManager class
            pokemon = Pokemon.objects.create(
                name=pokemon_response['name'],
                description='')
            pokemon.save()

            for ability_index in range(len(pokemon_response['abilities'])):
                ability_url = pokemon_response['abilities'][ability_index]['ability']['url']
                ability_response = requests.get(ability_url).json()
                ability = Ability.objects.create(
                    name=ability_response['name'],
                    is_main_series=ability_response['is_main_series'],
                    pokemon=pokemon)
                ability.save()


            # generation = Generation.objects.create()

            # To improve we could do a get or create (e.g. if the ability already exists don't greate a duplicate)




        # TODO Get pagination to work - use the next in the api resource = The URL for the next page in the list
        # it's the offset that keeps changing on every page
        # first_page = session.get(POKE_API_URL).json()
        # page_count = math.ceil(first_page['count'] / 20)
        # print(len(first_page['results']))
        # # yield first_page -  not needed if I save straight away
        #
        # for page in range(2, 5):
        #     next_page = session.get(POKE_API_URL, params={'limit': 20, 'offset': an_offset_variable_here}).json()
        #     print(next_page)

        return pokemon_count
