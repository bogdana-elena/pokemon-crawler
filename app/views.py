from django.http import HttpResponse
from django.views.generic import TemplateView

from app.crawler import PokemonCrawler


class PokemonView(TemplateView):
    template_name = "pokemon.html"

    def get(self, request, **kwargs):
        # make calls to the api - could be a task??
        pokemon_crawler = PokemonCrawler()
        pokemon_count = pokemon_crawler.crawl()

        # make a pokemon serializer and return?? or add to context for the template

        return HttpResponse(pokemon_count)
