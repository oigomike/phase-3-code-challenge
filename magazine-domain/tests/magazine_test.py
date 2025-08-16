import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

def test_magazine_articles_and_contributors():
    mag = Magazine("TechMag", "Tech")
    a1 = Author("Alice")
    a2 = Author("Bob")
    
    a1.add_article(mag, "AI Today")
    a2.add_article(mag, "Blockchain")
    a1.add_article(mag, "Quantum Computing")
    
    articles = mag.articles()
    contributors = mag.contributors()
    
    assert len(articles) == 3
    assert a1 in contributors
    assert a2 in contributors

def test_article_titles_and_contributing_authors():
    mag = Magazine("ScienceMag", "Science")
    a = Author("David")
    
    a.add_article(mag, "Physics")
    a.add_article(mag, "Chemistry")
    a.add_article(mag, "Biology")
    
    titles = mag.article_titles()
    top_authors = mag.contributing_authors()
    
    assert "Physics" in titles
    assert a in top_authors

def test_top_publisher():
    from lib.magazine import Magazine
    from lib.author import Author
    from lib.article import Article

    Magazine.all_magazines.clear()
    Article.all_articles.clear()

    mag1 = Magazine("Tech1", "Tech")
    mag2 = Magazine("Tech2", "Tech")
    author = Author("Eve")

    author.add_article(mag1, "Article1")
    author.add_article(mag1, "Article2")
    author.add_article(mag2, "Article3")

    top = Magazine.top_publisher()
    assert top == mag1

