from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic Model: Model with type specifications
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


# Always specify paths from most specific to least specific so that they get matched correctly.

# FastAPI will know that q is optional because of the = None. The Optional in Optional[str] is not used by FastAPI (FastAPI will only use the str part), but the Optional[str] will let your editor help you finding errors in your code.

# Query Parameter

@app.get('/blog')
async def index(limit=10, published: bool=True, sort: Optional[str]=None):
    if published:
        return {'data': f'{limit} published blogs from the db'}

    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
async def unpublished():
    return {'data': 'all unpublished blogs'}


# Path Parameter
# default type is String. Specify the type in the function to change it
@app.get('/blog/{id}')
async def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
async def comments(id: int):
    return {'data': {'1', '2', '3'}}


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created successfully with title {blog.title}'}

