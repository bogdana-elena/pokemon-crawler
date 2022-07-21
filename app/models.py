from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=60)
    # TODO find out how to construct and get creative with the description
    description = models.CharField(max_length=250)


class Ability(models.Model):
    name = models.CharField(max_length=60)
    is_main_series = models.BooleanField(default=False)
    pokemon = models.ForeignKey(
        'Pokemon',
        on_delete=models.DO_NOTHING
    )


class Generation(models.Model):
    name = models.CharField(max_length=60)
    ability = models.ForeignKey(
        'Ability',
        on_delete=models.DO_NOTHING
    )