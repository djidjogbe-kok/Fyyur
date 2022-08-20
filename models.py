from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(12),nullable=False,unique=True)
    genres = db.Column(db.ARRAY(db.String),nullable=False)
    image_link = db.Column(db.String(400))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(800))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    shows = db.relationship("Show", backref="venues", lazy=False, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Venue ID: {self.id}, name: {self.name}, city: {self.city},\
          state: {self.state},address:{self.address}, phone:{self.phone},\
            genres:{self.genres},image_link:{self.image_link},facebook_link:{self.facebook_link},\
              website_link:{self.website_link},seeking_artists:{self.seeking_artists},\
                seeking_description:{self.seeking_description}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False,unique=True)
    city = db.Column(db.String(120),nullable=False)
    state = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(12),nullable=False,unique=True)
    genres = db.Column(db.ARRAY(db.String),nullable=False)
    image_link = db.Column(db.String(400))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue=db.Column(db.Boolean,nullable=False,default=False)
    seeking_description=db.Column(db.String(800))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    shows = db.relationship("Show", backref="artists", lazy=False, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Artist ID: {self.id}, name: {self.name}, city: {self.city},\
          state: {self.state},phone:{self.phone},\
            genres:{self.genres},image_link:{self.image_link},facebook_link:{self.facebook_link},\
              website_link:{self.website_link},seeking_venue:{self.seeking_venue},\
                seeking_description:{self.seeking_description}>'
# TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    artists_id = db.Column(db.Integer,db.ForeignKey('artists.id'), nullable=False)
    venues_id = db.Column(db.Integer,db.ForeignKey('venues.id'),nullable=False)
    start_time=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f'<Show ID: {self.id}, artists_id: {self.artists_id}, venues_id:{self.venues_id}, start_time: {self.start_time}>'