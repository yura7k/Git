import mongoengine

class Booking(mongoengine.EmbeddedDocument):
    guest_id = mongoengine.ObjectIdField()
    booked_date = mongoengine.DateTimeField()
    chek_in_date = mongoengine.DateTimeField(required=False)
    chek_out_date = mongoengine.DateTimeField(required=False)

    @property
    def duration(self):
        dt = self.chek_out_date - self.chek_in_date
        return dt.days

    """meta = {
        'db_alias': 'hotel',
        'collection': 'bookings'
    }"""