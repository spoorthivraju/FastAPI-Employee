#Standard Library Imports
import uuid

#Third Party Imports
from sqlalchemy import String, Integer, VARCHAR, ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import relationship

#Local Application Imports
from app.src.database import Base
from app.models.department import Department
from app.models.address import Address


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(VARCHAR(25), nullable=True)
    last_name = Column(VARCHAR(25), nullable=True)
    email = Column(VARCHAR(60), nullable=True)
    department_id = Column(UUID(as_uuid=True), ForeignKey(Department.__table__.c.id), nullable=True)
    address_id = Column(UUID(as_uuid=True), ForeignKey(Address.__table__.c.id), nullable=True)

    


 