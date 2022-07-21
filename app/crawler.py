import math
import logging
import requests

from app.models import Pokemon, Ability

logger = logging.getLogger(__name__)

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon'

session = requests.Session()


def calculate_pokemon_description(pokemon_response):
    description = ''

    if len(pokemon_response['types']) == 1:
        description = f"A {pokemon_response['types'][0]['type']['name']} pokemon"
    elif len(pokemon_response['types']) == 2:
        description = f"A {pokemon_response['types'][0]['type']['name']} and " \
                      f" {pokemon_response['types'][1]['type']['name']} pokemon"

    return description


def get_pokemon_hp(pokemon_response):
    for stat in pokemon_response['stats']:
        if stat['stat']['name'].lower() == 'hp':
            return stat['base_stat']
    return 100


def persist_pokemon_in_page(page):
    for pokemon_index in range(len(page['results'])):
        pokemon_url = page['results'][pokemon_index]['url']
        pokemon_response = session.get(pokemon_url).json()

        # A pokemon can have a maximum of two types
        description = calculate_pokemon_description(pokemon_response)
        hp = get_pokemon_hp(pokemon_response)

        # Use the get_or_create method to avoid duplicate pokemon being saved
        # pokemon_created is a boolean that indicates whether the pokemon was successfully created
        pokemon, pokemon_created = Pokemon.objects.get_or_create(
            name=pokemon_response['name'],
            description=description,
            base_experience=pokemon_response['base_experience'],
            weight=pokemon_response['weight'],
            height=pokemon_response['height'],
            hp=hp)

        if pokemon_created:
            # Look for the abilities of the current pokemon and save them to the database
            for ability_index in range(len(pokemon_response['abilities'])):
                ability_url = pokemon_response['abilities'][ability_index]['ability']['url']
                ability_response = requests.get(ability_url).json()
                ability, ability_created = Ability.objects.get_or_create(
                    name=ability_response['name'],
                    is_main_series=ability_response['is_main_series'],
                    pokemon=pokemon)


class PokemonCrawler:
    @staticmethod
    def crawl():
        # For pagination get the next page url from the api resource
        # it's the offset that keeps changing on every page
        try:
            first_page = session.get(POKE_API_URL).json()
        except Exception:
            logger.error(f'Failed to reach: {POKE_API_URL}')
            return 0

        pokemon_count = first_page['count']
        # Round up so that if the number of pokemon is not a multiplier of 20 we get the ones on the last page
        page_count = math.ceil(pokemon_count / 20)
        next_page_url = first_page['next']

        persist_pokemon_in_page(first_page)

        try:
            for page in range(page_count):
                logger.info(f'Processing pokemon on page {page}...')
                next_page = session.get(next_page_url).json()
                next_page_url = next_page['next']

                persist_pokemon_in_page(next_page)
        except Exception:
            logger.error(f'Failed to reach: {next_page_url}')

        return pokemon_count

