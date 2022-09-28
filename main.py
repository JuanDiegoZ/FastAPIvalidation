#python.
from ast import Lt
from operator import le, lt
import string
from typing import Optional
#Pydantic.
from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()
#Models
class Location(BaseModel):
    city: str
    state: str
    country: str
    
    
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
    name: Optional[str] =  Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="this parameter is optional, Name of individual" 
        ),
    age: Optional[int] = Query(
        0,
        gt=0,
        lt=100,
        title="Person age",
        description="The age is optional, has to be less than 100"
        )
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


#Validacion: Path parameters.
@app.get("/person/detail/{person_id}")
def show_person_detail(
    person_id: str = Path(
        ...,
        min_length=6,
        title ="Number id of the person.",
        description="This parameter is required,Identification of the person."
        )
    
):
    return {person_id : "It exists!"}

#Validaciones: Request Body.

@app.put("/person/{person_id}") 
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt = 0
        ),
    person: Person = Body(...),
    location: Location = Body(...)   
) -> Person:
    result = dict(person)
    result.update(dict(location))
    return result

