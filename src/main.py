from src.imdbrefining import namesIMDB
from src.twitterAPI import twitterSearch
from src.download_files import download_files

def main():
    download_files.Download_files().download_files_imdb()
    top_actors_name_list = namesIMDB.NamesIMDB().get_top_actors()
    tweets = twitterSearch.TwitterSearch().search_tweets_of_actors_list(top_actors_name_list)
    twitterSearch.TwitterSearch().convert_to_csv(tweets)

if __name__ == '__main__':
    main()
