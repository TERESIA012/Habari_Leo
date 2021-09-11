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
    
    return render_template('index.html',my_news=my_news)



@main.route('/news/<id>')
def news_articles(id):

    """
    View articles function
    """
    articles=get_article(id)
    
    return render_template('articles.html',articles=articles)

    
@main.route('/category/<category>')
def acquire_category(category):
    
    """
    View category function
    """

    category=get_category(category)
    return render_template('news.html',category=category)


# @main.route('/articles/<id>')
# def article(id):

#     '''
#     View article page function that returns the various article details page and its data
#     '''
#     my_article=article_source(id)
#     title=f'{id}'
   
    
    
#     return render_template('articles.html',my_article=my_article,title=title )








