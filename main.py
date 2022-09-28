#python.
import string
from typing import Optional
#Pydantic.
from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI
from fastapi import Body

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