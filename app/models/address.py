#Standard Library Imports
import uuid

#Third Party Imports
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.sql.schema import Column
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import relationship

#Local Application Imports
from app.src.database import Base
from app.models.state import State 
#from app.models.employee import Employee
from app.models.country import Country


class Address(Base):
    __tablename__ = 'address'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    address = Column(VARCHAR(125), nullable=True)
    city = Column(VARCHAR(25), nullable=True)
    state_id = Column(UUID(as_uuid=True), ForeignKey(State.__table__.c.id), nullable=True)
    country_id = Column(UUID(as_uuid=True), ForeignKey(Country.__table__.c.id), nullable=True)