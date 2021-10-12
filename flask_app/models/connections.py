
# mongo-engine packages
from mongoengine import Document, StringField, IntField, ListField


class NodeConnections(Document):
    """
    Template for a mongoengine document, which represents the connections to a given Gare du Nord platform
    It also lists conflicts with trains coming from other Nord platforms
    """

    connection_id = IntField(required=True)
    node_from = StringField(required=True)
    node_to = StringField(required=True)


class Conflicts(Document):
    """
    Template for a mongoengine document, which represents the connections to a given Gare du Nord platform
    It also lists conflicts with trains coming from other Nord platforms
    """

    conflict_id = IntField(required=True)
    connection_id1 = IntField(required=True)
    connection_id2 = IntField(required=True)


