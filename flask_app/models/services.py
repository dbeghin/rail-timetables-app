
# mongo-engine packages
from mongoengine import Document, StringField, IntField


class Services(Document):
    """
    Template for a mongoengine document, which represents a user's favorite meal.
    :param name: required string value
    :param description: optional string value, fewer than 240 characters
    :param price: optional float value
    :param image_url: optional string image url
    """

    service = StringField(required=True)
    operator = StringField()
    tph = IntField()
    line_north = StringField()
    line_south = StringField()



class ServiceFlows(Document):
    """
    Template for a mongoengine document, which represents a user's favorite meal.
    :param name: required string value
    :param description: optional string value, fewer than 240 characters
    :param price: optional float value
    :param image_url: optional string image url
    """

    service_number = StringField()
    service = StringField(required=True)
    direction = StringField()
    platform_nord = StringField()
    platform_central = StringField()
    platform_midi = StringField()



class Trains(Document):
    """
    Template for a mongoengine document, which represents a user's favorite meal.
    :param name: required string value
    :param description: optional string value, fewer than 240 characters
    :param price: optional float value
    :param image_url: optional string image url
    """

    train_number = StringField(required=True)
    service_number = StringField()
    arrival_nord = IntField()
    departure_nord = IntField()
    arrival_central = IntField()
    departure_central = IntField()
    arrival_midi = IntField()
    departure_midi = IntField()
