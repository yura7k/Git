import mongoengine
from models.booking import Booking

class Apartment(mongoengine.Document):
    name = mongoengine.StringField(required=True, unique=True)
    price = mongoengine.FloatField(required=True, min_value=15)
    description = mongoengine.StringField()
    smoke_allowed = mongoengine.BooleanField(default=False)

    bookings = mongoengine.EmbeddedDocumentListField(Booking)
   
    meta = {
        'db_alias': 'hotel',
        'collection': 'apartments'
    }