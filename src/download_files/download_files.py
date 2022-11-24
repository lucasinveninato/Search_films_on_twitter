from wget import download as wget_download
from os import path, mkdir, remove, getcwd
import logging
from logging import config


config.fileConfig("./src/logger.conf", disable_existing_loggers = False)
logger = logging.getLogger(__name__)


class Download_files():

    def __init__(self):
        self.url_list = ['https://datasets.imdbws.com/name.basics.tsv.gz',
                        'https://datasets.imdbws.com/title.basics.tsv.gz',
                        'https://datasets.imdbws.com/title.principals.tsv.gz']
        
        self.data_source = path.join(getcwd(), r'imdbdatabase')

    def download_files_imdb(self):
        try:
            logger.info('downloading files')

            if not path.isdir(self.data_source): mkdir(self.data_source)

            for url in self.url_list:
                if not isinstance(url, str):
                    message = f"Environment variable name must be a string."
                    raise TypeError(message)

                file_path = path.join(self.data_source, self.__split_name(url))
                if path.exists(file_path): remove(file_path)
                wget_download(url, path.join(self.data_source, file_path))
                logger.info(f'the file {self.__split_name(url)} has been successfully downloaded')
        
        except Exception as e:
            logger.error(e)
            raise

    def __split_name(self, url):
        split_url = url.split('/')
        file_name = split_url.pop()
        return file_name
