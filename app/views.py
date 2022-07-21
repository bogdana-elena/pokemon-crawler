from django.http import HttpResponse
from django.views.generic import TemplateView

from app.crawler import PokemonCrawler

import logging

logger = logging.getLogger(__name__)


class PokemonView(TemplateView):
    template_name = "pokemon.html"

    def get(self, request, **kwargs):
        logger.info("Pokemon crawl has started...")
        pokemon_count = PokemonCrawler.crawl()

        return HttpResponse(f"Pokemon crawl finished. {pokemon_count} possible pokemon found.")
