from sqlalchemy import Column, String, Integer, Date

from base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    type_no = Column(String)
    name = Column(String)
    location = Column(String)
    password = Column(String)

    def __init__(self, type_no, name, location, password):
        self.type_no = type_no
        self.name = name
        self.location = location
        self.password = password

class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    category = Column(String)
    model = Column(String)
    serial = Column(String)
    location = Column(String)
    return_date = Column(Date) 
    from_id = Column(Integer)
    to_id = Column(Integer)
    remarks = Column(String)

    def __init__(self, category, model, serial, location, return_date, from_id, to_id, remarks):
        self.category = category
        self.model = model
        self.serial = serial
        self.location = location
        self.return_date = return_date
        self.from_id = from_id
        self.to_id = to_id
        self.remarks = remarks

class Request(Base):
    __tablename__ = "requests"
    
    id = Column(Integer, primary_key=True)
    type_no = Column(String)
    date = Column(Date)
    requester = Column(Integer)
    to_id = Column(Integer)
    from_id = Column(Integer)
    status = Column(Integer)
    serials = Column(String)
    action = Column(String)

    def __init__(self, type_no, date, requester, to_id, from_id, status, serials, action):
            self.type_no = type_no
            self.date = date
            self.requester = requester
            self.to_id = to_id
            self.from_id = from_id
            self.status = status
            self.serials = serials
            self.action = action
