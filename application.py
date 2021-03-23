from typing import List

from fastapi import Depends, FastAPI, Body
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

from datetime import date, datetime
from typing import Optional
from uuid import UUID

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Application Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=List[schema.ServiceBase])
async def read_items(
    # id: UUID,
    start_datetime: Optional[date] = Body(None),
    end_datetime: Optional[date] = Body(None),
    db: Session = Depends(get_db),
):

    movies = crud.get_data(db=db)
    return movies
    

