import mongoengine
from models.booking import Booking

class Apartment(mongoengine.Document):
    name = mongoengine.StringField(required=True, unique=True)
    price = mongoengine.FloatField(required=True, min_value=15)
    description = mongoengine.StringField()
    smoke_allowed = mongoengine.BooleanField(default=False)

    booking = mongoengine.EmbeddedDocumentListField(Booking)
    #  як варіант
    #  booking = ListField(mongoengine.EmbeddedDocumentField(Booking))
    #
    #
    #

    meta = {
        'db_alias': 'hotel',
        'collection': 'apartments'
    }