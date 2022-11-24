from pandas import DataFrame, concat
import tweepy as tw
from os import path, mkdir, getcwd, remove, environ
import logging
from logging import config
import dotenv
from dotenv import load_dotenv


config.fileConfig("./src/logger.conf", disable_existing_loggers = False)
logger = logging.getLogger(__name__)

class TwitterSearch():
    def __init__(self):
        pass

    def twitter_api(self):
        try:
            load_dotenv(dotenv_path =  'src/.env')
            auth = tw.OAuthHandler(environ['API_KEY'], environ['API_KEY_SECRET'])
            auth.set_access_token(environ['ACCESS_TOKEN'], environ['ACCESS_TOKEN_SECRET'])
            api = tw.API(auth, wait_on_rate_limit=True)
            return api
        
        except Exception as e:
            logger.error(e)
            raise
        
    def search_tweets_of_actor(self, name):
        try:
            api = self.twitter_api()
            users = []
            tweets = []
            created_at = []
            tweet_id = []
            results = api.search_tweets(q=name, count=10)

            for tweet in results:
                users.append(tweet.user.name)
                tweets.append(tweet.text)
                created_at.append(tweet.created_at)
                tweet_id.append(tweet.id)
                
            logger.info(f'{name} : {len(results)} results from twitter')
            df_tweets = DataFrame() 
            df_tweets['created_at'] = created_at
            df_tweets['users'] = users
            df_tweets['tweet_id'] = tweet_id
            df_tweets['tweets'] = tweets
            return df_tweets
        
        except Exception as e:
            logger.error(e)
            raise

    def search_tweets_of_actors_list(self, actors_name_list):
        try:
            logger.info('Searching tweets related to top actors list')
            df_tweets_of_top_actors = DataFrame()
            for actor in actors_name_list:
                tweets_of_actor = self.search_tweets_of_actor(actor)
                df_tweets_of_top_actors = concat([df_tweets_of_top_actors, tweets_of_actor], sort=False)
                
            df_tweets = DataFrame.from_dict(df_tweets_of_top_actors)
            logger.info('Tweets were found')
            return df_tweets
        
        except Exception as e:
            logger.error(e)
            raise

    def convert_to_csv(self, df_tweets):
        try:
            logger.info('Saving tweets')
            path_dir = path.join(getcwd(), 'src/output/data/')
            path_file = path.join(path_dir, 'tweetsoftop10actors.csv')
            if not path.isdir(path_dir): mkdir(path_dir)
            if path.exists(path_file): remove(path_file)
            df_tweets.to_csv(path_file, index=False, sep=';')
            logger.info(f'The tweets were saved in the path: {path_file}')
        
        except Exception as e:
            logger.error(e)
            raise

