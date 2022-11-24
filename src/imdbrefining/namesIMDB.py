from src.imdbrefining import movies
from src.imdbrefining import actors

class NamesIMDB():
    def __init__(self):
        self.movies = movies.Movies()
        self.actors = actors.Actors()

    def get_top_actors(self):
        movies2012 = self.movies.all_movies_id_from_year(2012)
        actors_id = self.actors.actors_id_on(movies2012)
        top_actors_id = self.actors.top_actors_id(actors_id, 10)
        top_actors_name_list = self.actors.top_actors_name_list(top_actors_id)
        return top_actors_name_list
