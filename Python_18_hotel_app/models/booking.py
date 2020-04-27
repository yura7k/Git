import mongoengine
from models.guests import Guest

class Booking(mongoengine.EmbeddedDocument):
    guest_id = mongoengine.ReferenceField(Guest)
    booked_date = mongoengine.DateTimeField()
    chek_in_date = mongoengine.DateTimeField(required=True)
    chek_out_date = mongoengine.DateTimeField(required=True)

    @property
    def duration(self):
        data = self.chek_out_date - self.chek_in_date
        return data.days