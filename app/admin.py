from django.contrib import admin
from .models import Pokemon, Ability, Generation


class PokemonAdmin(admin.ModelAdmin):
    model = Pokemon
    search_fields = ["name"]
    list_display = (
        "name",
        "description",
        "base_experience",
        "hp",
    )


class AbilityAdmin(admin.ModelAdmin):
    model = Ability
    search_fields = ["name"]
    list_display = (
        "name",
        "is_main_series",
        "pokemon",
    )
    raw_id_fields = (
        "pokemon",
    )


class GenerationAdmin(admin.ModelAdmin):
    model = Generation
    search_fields = ["name"]
    list_display = (
        "name",
        "ability",
    )
    raw_id_fields = (
        "ability",
    )


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Generation, GenerationAdmin)
