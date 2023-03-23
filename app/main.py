#Third Party Imports
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import status
from typing import List
import json
from sqlalchemy import select


#Local Application Imports
from app.models import employee
from app.models.employee import Employee
from app.models.department import Department
from app.models.address import Address
from app.models.state import State
from app.models.country import Country
from app.schemas.employee import CreateEmployee
from app.src.database import get_db
from fastapi.responses import JSONResponse
#from models import Employee

app = FastAPI()

@app.post("/")
def create_employee(details: CreateEmployee, db: Session = Depends(get_db)):

    try:

        employee_address = {
            'address' : details.address,
            'city' : details.city,
            'state_id' : details.state_id,
            'country_id' : details.country_id
        }

        employee_details = {
        'first_name' : details.first_name,
        'last_name' : details.last_name,
        'email' : details.email,
        'department_id' : details.department_id
        }

        addr_id = (db.query(Address.id).filter(
            Address.address == employee_address['address'],
            Address.city == employee_address['city'],
            Address.state_id == employee_address['state_id'],
            Address.country_id == employee_address['country_id']
            ).first()
        )

        if not addr_id :
            obj = jsonable_encoder(employee_address)
            db.add(Address(**obj))
            db.commit()
        
        addr_id = (db.query(Address.id).filter(
            Address.address == employee_address['address'],
            Address.city == employee_address['city'],
            Address.state_id == employee_address['state_id'],
            Address.country_id == employee_address['country_id']
            ).first()[0]
        )

        employee_details.update({'address_id' : addr_id})
        obj = jsonable_encoder(employee_details)
        db.add(Employee(**obj))
        db.commit()


        return JSONResponse(
            status_code = 200, 
            content = {'message': "Record created successfully"}
                              )

    except Exception as e:
        print(e)



@app.get("/") #, response_model=EmployeeResponse, status_code=200
def get_employees(db: Session = Depends(get_db)):
    print("something")

    try:  
        records = db.query(Employee).all()
        #response =  jsonable_encoder(records)

        
        return records
        
    
    
    except Exception as e:
        print(e)