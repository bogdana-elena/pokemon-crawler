from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=250, help_text="Type of pokemon")
    base_experience = models.IntegerField(null=True, default=0)
    weight = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    hp = models.IntegerField(default=100)


class Ability(models.Model):
    name = models.CharField(max_length=60)
    is_main_series = models.BooleanField(default=False)
    pokemon = models.ForeignKey(
        'Pokemon',
        on_delete=models.SET_NULL,
        null=True,
    )


class Generation(models.Model):
    name = models.CharField(max_length=60)
    ability = models.ForeignKey(
        'Ability',
        on_delete=models.SET_NULL,
        null=True,
    )
