from pandas import concat, read_table
from os import path, getcwd
import logging
from logging import config


config.fileConfig("./src/logger.conf", disable_existing_loggers = False)
logger = logging.getLogger(__name__)


class Movies():
    def __init__(self):
        self.title_basics_database = path.join(getcwd(), 'imdbdatabase', 'title.basics.tsv.gz')

    def all_movies_id_from_year(self, from_year: int):
        try:
            if not path.exists(self.title_basics_database):
                raise FileNotFoundError (f'{self.title_basics_database} does not exist.')
        
            logger.info(f'Looking for movies from year {from_year}')
            columns = ['tconst', 'titleType', 'startYear']
            chunk_size = 100000
            movies_df = []
            load = read_table(self.title_basics_database, compression='gzip', usecols=columns, dtype= { 'titleType': 'category', 'startYear': 'string'}, chunksize=chunk_size)
            for chunk in load:
                df = chunk
                df.loc[(df.startYear == r'\N'), 'startYear'] = '0000'
                df['startYear'] = df['startYear'].astype(int)
                df = df.loc[(df['titleType'] == 'movie')]
                df = df.loc[(df['startYear'] >= from_year)]
                df = df['tconst']     
                if not df.empty:
                    movies_df.append(df)         
            all_movies_df = concat(movies_df)
            logger.info('Movies were Found')
            return all_movies_df
        
        except Exception as e:
            logger.error(e)
            raise