from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_article, get_category, get_news




#Views
@main.route('/')
def index():
    

    '''
    View root page function that returns the index page and its data
    '''
    
    my_news=get_news()
    category=get_category('sports')
    return render_template('index.html',my_news=my_news,category=category)



@main.route('/news/<id>')
def news_articles(id):

    """
    View articles function
    """
    articles=get_article(id)
    
    return render_template('articles.html',articles=articles)


@main.route('/general')
def show_articles():
    """
    Show articles function
    """
    category=get_category('general')
    return render_template('general.html',category=category)


@main.route('/technology')
def show_technology():
    """
    Show articles function
    """
    category=get_category('technology')
    return render_template('technology.html',category=category)



@main.route('/health')
def show_health():
    """
    Show articles function
    """
    category=get_category('health')
    return render_template('afya.html',category=category)


    
    

    








