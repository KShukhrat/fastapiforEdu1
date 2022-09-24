from typing import List
from fastapi import FastAPI, Query, Path, Body
from scheamas import Author, Book

app = FastAPI()


# @app.get('/')
# def home():
#     return {'key':'hello'}


# @app.get('/{pk}')
# def get_item(pk:int, q: int = None):
#     return {'key':pk, 'q':q}   

# @app.get('/user/{pk}/item/{item}')
# def get_item(pk:int,item : str):
#     return {'key':pk, 'item': item}   
  
 
@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {'item': item, 'author': author, 'quantity': quantity}

@app.post('/author')
def add_author(author: Author = Body(..., embed=True)):#embeds jsondagi tartibini tugirliydi
    return {'author': author}
@app.get('/book')
def get_book(q:List[str] = Query(['test','test2'], description='Search book', deprecated=True)):
    return q

@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):#gt=min le=max
    return {'pk': pk, 'pages': pages}