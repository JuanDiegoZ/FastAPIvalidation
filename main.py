#python.
from ast import Lt
from operator import le, lt
import string
from typing import Optional
#Pydantic.
from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()
#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    weight: Optional[int] = None
    sex: Optional[str] = None
    



@app.get("/")
def home():
    """_summary_
        Args:
            None
        
        return
            Hello World in .json to API  
        
    """
    return{"hello":"world"}

#Request and Response Body.

@app.post("/person/new")
def create_person(persona: Person = Body(...)) -> Person:
    """_summary_

    Args:
        persona (Person, optional): _description_. Defaults to Body(...).

    Returns:
        Person: _description_
    """
    return persona

#Validation: Query parameters.
@app.get("/person/new")
def show_person( 
    name: Optional[str] =  Query(None,min_length=1,max_length=50),
    age: Optional[int] = Query(0,gt=1,lt=50)
    ):
    """_summary_
        This fuction use a decorator, Query with

    Args:
        name (Optional[str], optional): _description_. Defaults to Query(None,min_length=1,max_length=50).
        age (Optional[int], optional): _description_. Defaults to Query(0,min_length=1,max_length=150).

    Returns:
        _int_: _age whit name_
    """
    return {name : age}



