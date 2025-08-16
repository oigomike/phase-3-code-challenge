import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

def test_article_properties():
    mag = Magazine("FunMag", "Lifestyle")
    author = Author("Frank")
    art = author.add_article(mag, "Travel Tips")
    
    assert art.title == "Travel Tips"
    assert art.author == author
    assert art.magazine == mag

def test_changing_author_and_magazine():
    mag1 = Magazine("Mag1", "Category1")
    mag2 = Magazine("Mag2", "Category2")
    author1 = Author("Grace")
    author2 = Author("Hank")
    
    art = author1.add_article(mag1, "Cool Article")
    art.set_author(author2)
    art.set_magazine(mag2)
    
    assert art.author == author2
    assert art.magazine == mag2
