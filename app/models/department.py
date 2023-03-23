#Standard Imports
import uuid

#Third Party Imports
from sqlalchemy import VARCHAR
from sqlalchemy.sql.schema import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

#Local Application Imports
from app.src.database import Base


class Department(Base):
    __tablename__ = 'department'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    department = Column(VARCHAR(25), nullable=True)

    #emp_department = relationship(Employ, backref=True)

    #employee_department = relationship(Department, backref=True)
