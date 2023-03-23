#Standard Imports
import uuid

#Third Party Imports
from sqlalchemy import VARCHAR
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

#Local Application Imports
from app.src.database import Base

class Country(Base):
    __tablename__ = 'country'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    country_name = Column(VARCHAR(25), nullable=True)