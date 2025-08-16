import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

def test_author_name():
    a = Author("Alice")
    assert a.name == "Alice"

def test_author_articles_and_magazines():
    mag1 = Magazine("TechTimes", "Tech")
    mag2 = Magazine("HealthMag", "Health")
    author = Author("Bob")
    
    author.add_article(mag1, "Tech News")
    author.add_article(mag2, "Healthy Living")
    
    articles = author.articles()
    magazines = author.magazines()
    
    assert len(articles) == 2
    assert mag1 in magazines
    assert mag2 in magazines

def test_topic_areas():
    mag1 = Magazine("Foodie", "Food")
    author = Author("Carol")
    author.add_article(mag1, "Cooking Tips")
    
    topics = author.topic_areas()
    assert "Food" in topics
