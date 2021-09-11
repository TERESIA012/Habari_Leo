import os

class Config:

    NEWS_API_SOURCE_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_ARTICLE_KEY = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SECRET_KEY = os.urandom(32)


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
    
    
    