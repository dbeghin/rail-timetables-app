# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# mongo-engine models
from models.connections import NodeConnections, Conflicts
from models.users import Users
from api.errors import forbidden


class NodeConnectionsApi(Resource):
    @jwt_required()
    def get(self):
        output = NodeConnections.objects()
        resp = jsonify(output)
        return resp


    @jwt_required()
    def post(self) -> Response:
        """
        POST response method for creating meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin
        authorized = True
        
        if authorized:
            data = request.get_json()
            post_user = NodeConnections(**data).save()
            output = {'connection_id': str(post_user.connection_id)}
            return jsonify({'result': output})
        else:
            return forbidden()



class NodeConnectionApi(Resource):
    """
    Flask-resftul resource for returning db.ConnectionsNorth collection.
    """
    @jwt_required()
    def get(self, connection_id: str) -> Response:
        """
        GET response method for single documents in meal collection.
        :return: JSON object
        """
        output = NodeConnections.objects.get(connection_id=connection_id)
        return jsonify({'result': output})


    @jwt_required()
    def delete(self, connection_id: str) -> Response:
        """
        DELETE response method for deleting single meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = NodeConnections.objects(connection_id=connection_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()
    



class ConflictsApi(Resource):
    @jwt_required()
    def get(self):
        output = Conflicts.objects()
        return jsonify({'result': output})


    @jwt_required()
    def post(self) -> Response:
        """
        POST response method for creating meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Conflicts.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Conflicts(**data).save()
            output = {'conflict_id': str(post_user.conflict_id)}
            return jsonify({'result': output})
        else:
            return forbidden()



class ConflictApi(Resource):
    """
    Flask-resftul resource for returning db.ConnectionsNorth collection.
    """
    @jwt_required()
    def get(self, conflict_id: str) -> Response:
        """
        GET response method for single documents in meal collection.
        :return: JSON object
        """
        output = Conflicts.objects.get(conflict_id=conflict_id)
        return jsonify({'result': output})


    @jwt_required()
    def delete(self, conflict_id: str) -> Response:
        """
        DELETE response method for deleting single meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Conflicts.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Conflicts.objects(conflict_id=conflict_id).delete()
            return jsonify({'result': output})
        else:
            return forbidden()
    
