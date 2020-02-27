from app import db
from datetime import datetime


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    code = db.Column(db.String(8))  # короткое название ("nsk","msk","kzn","online")
    events = db.relationship("Event",  back_populates="location")


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    type = db.Column(db.String)
    category = db.Column(db.String)     # ["Python", "ML", "Управление проектами", "")
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    location = db.relationship("Location", back_populates="events")
    address = db.Column(db.String)  # адрес
    seats = db.Column(db.Integer)   # количество мест
    participants = db.relationship("Enrollment", back_populates="event")     # Участники


class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.Integer, primary_key=True)
    name_and_surname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    picture = db.Column(db.String)
    location = db.Column(db.String)
    about = db.Column(db.String)
    enrollments = db.relationship("Enrollment", back_populates="participant")


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    event = db.relationship("Event", back_populates="participants")
    participant_id = db.Column(db.Integer, db.ForeignKey("participants.id"))
    participant = db.relationship("Participant", back_populates="enrollments")


db.create_all()
