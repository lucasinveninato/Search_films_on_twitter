from pandas import read_table, DataFrame, concat
from os import path, getcwd
import logging
from logging import config


config.fileConfig("./src/logger.conf", disable_existing_loggers = False)
logger = logging.getLogger(__name__)

class Actors():
    def __init__(self):
        self.title_principals_database = path.join(getcwd(), 'imdbdatabase','title.principals.tsv.gz')
        self.name_basics_database = path.join(getcwd(), 'imdbdatabase', 'name.basics.tsv.gz')

    def actors_id_on(self, movies_id) : 
        try:
            logger.info('Looking for actors id')
            columns = ['tconst', 'nconst', 'category']
            chunk_size = 100000
            
            if not path.exists(self.title_principals_database):
                raise FileNotFoundError (f'{self.title_principals_database} does not exist.')

            actors_id_df = []
            load = read_table(self.title_principals_database, compression='gzip',usecols=columns, dtype= {'category': 'string', 'tconst': 'string', 'nconst': 'string'}, chunksize=chunk_size)
            for chunk in load:
                df = chunk
                df = df.merge(movies_id, how='inner', on=[('tconst')])
                df = df.loc[(df['category'] == 'actor') | (df['category'] == 'actress')]
                df = df['nconst']
                if not df.empty:
                    actors_id_df.append(df)         
            actors_id = concat(actors_id_df)
            logger.info('Actors id were found')
            return actors_id
    
        except Exception as e:
            logger.error(e)
            raise
        
    def top_actors_id(self, actors_id_df, index_of_top):
        try:
            logger.info(f'Looking for id of top {index_of_top} actors with most performance')
            df = DataFrame(actors_id_df)   
            df = df.groupby(['nconst']).value_counts()
            df = df.sort_values(ascending=False)
            id_top_actors_list = df.index.tolist()[:index_of_top]
            logger.info(f'top {index_of_top}: {id_top_actors_list}')
            return id_top_actors_list
        
        except Exception as e:
            logger.error(e)
            raise

    def top_actors_name_list(self, id_top_actors_list):
        try:
            logger.info('Looking for Actors names')
            columns = ['nconst', 'primaryName']
            chunk_size = 10000
            
            if not path.exists(self.name_basics_database):
                raise FileNotFoundError (f'{self.title_principals_database} does not exist.')

            load = read_table(self.name_basics_database, compression='gzip', usecols=columns, dtype= {'primaryName': 'string', 'nconst': 'string'}, chunksize=chunk_size)
            df_id_actors = []
            for chunk in load:
                for actor_id in id_top_actors_list:
                    part = chunk[ chunk['nconst'] == actor_id ]
                    df_id_actors.append(part)

            id_actors = concat(df_id_actors)
            list_actor_names = id_actors['primaryName'].tolist()           
            logger.info(f'top actors list name: {list_actor_names}')
            return list_actor_names
        
        except Exception as e:
            logger.error(e)
            raise
