from sqlalchemy import Column, Integer, String, Date, Float
from db_handler import Base


class Service(Base):
    """
    This is a model class. which is having the movie table structure with all the constraint
    """
    __tablename__ = "service_availabilities"
    #P_id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    
    date = Column(Date, primary_key=True, index=True, nullable=False)
    service = Column(String, index=True, nullable=False)
    availability = Column(Float, index=True, nullable=False)
    # P_id = Column(Integer, primary_key=True, autoincrement=True)