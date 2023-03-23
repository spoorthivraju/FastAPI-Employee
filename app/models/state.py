#Standard Imports
import uuid

#Third Party Imports
from sqlalchemy import String, Integer, ForeignKey, VARCHAR
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

#Local Application Imports
from app.src.database import Base
from app.models.country import Country



class State(Base):
    __tablename__ = 'state'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    state_name = Column(VARCHAR(25), nullable=True)
    country_id = Column(UUID(as_uuid=True), ForeignKey(Country.__table__.c.id), nullable=True)