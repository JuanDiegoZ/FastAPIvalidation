#python.
from doctest import Example
import email
from enum import Enum
from typing import Optional
#Pydantic.
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()
#Models

class Hair_color(Enum):
    blue = "blue"
    black = "black"
    white = "white"
    brown = "brown"
    red = "red"
    other = "other"
    
class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Cajica"
        )
    state: str = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Cundinamarca"
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=100,
        example="Colombia"
        )
    
    
class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length= 50,
        )
    age: int =  Field(
        ...,
        gt=0,
        le=150
    )
    email: EmailStr = Field(
        ...,
        Example="123mail@mail.com"
        )
    
    hair_color: Optional[Hair_color]= Field(default=None)
    weight: Optional[int] = Field(default=None)
    sex: Optional[str] = Field(default=None)
    



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
        description="this parameter is optional, Name of individual",
        example= "Pepe" 
        ),
    age: Optional[int] = Query(
        0,
        gt=0,
        lt=100,
        title="Person age",
        description="The age is optional, has to be less than 100",
        example=20
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
        gt = 0,
        example=123
        ),
    person: Person = Body(...),
    location: Location = Body(...)   
) -> Person:
    result = dict(person)
    result.update(dict(location))
    return result

