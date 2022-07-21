# Pokemon Crawler

Django app that crawls the PokeApi and persists pokemon data: https://pokeapi.co/
Project started from https://github.com/cybsafe/pokemon-crawler

### Requirements:

* Python 3
* Docker: https://docs.docker.com/compose/install/
* PostrgreSQL: https://www.postgresql.org/download/ (or use brew)

### To run:
 
Clone the repo then from the pokemon-crawler folder run:
* `docker-compose up`
* `docker-compose exec web python -m pip install -r requirements.txt`

If there are any migrations needed:
* `docker-compose exec web python manage.py migrate`

Then browse to: http://localhost:8000/pokemon/
This will automatically trigger the crawler and pokemon data will start to be populated in the database.

To see the data go to: http://localhost:8000/admin/
There will be 3 tables created under APP: Abilitys, Generations, Pokemons



### Future improvements:
* Use pagination (the url for the next page can be extracted from the response)
* Add data validation and checks for uniqueness (so we don't save a pokemon, ability or generation twice)
* Persist more stats and abilities
* Add error handling and logs
* Use the Django template to add a button that triggers the crawler 
* Display the data via the Django template 
* Add tests for the views, models and crawler (by mocking the API response)

* Use the pokemon data to create contests between them in a responsive Django web app