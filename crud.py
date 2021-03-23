from sqlalchemy.orm import Session
import model
import schema

def get_data(db: Session):
    """
    This method will return single all the details
    """
    obj_list = db.query(model.Service).all()
    result = []
    for obj in obj_list:
        user = {}
        user['date'] = object[0]
        user['service'] = object[1]
        user['availability'] = object[2]
        result.append(user)
         
    return result


