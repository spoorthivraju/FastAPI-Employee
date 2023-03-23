#Standard Library Imports
#import uuid

#Third Party Imports
from pydantic import BaseModel
from typing import List

class CreateEmployee(BaseModel):
    first_name : str
    last_name : str
    email : str
    department_id : str
    address : str
    city : str
    state_id : str
    country_id : str

    class config:
        orm_mode = True