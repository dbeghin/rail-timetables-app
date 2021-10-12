# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# mongo-engine models
from models.services import Services, ServiceFlows, Trains
from models.users import Users
from api.errors import forbidden


#General information about services
class ServicesApi(Resource):
    @jwt_required()
    def get(self):
        output = Services.objects()
        return jsonify({'result': output})


    @jwt_required()
    def post(self) -> Response:
        """
        POST response method for creating meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Services(**data).save()
            output = {'service': str(post_user.service)}
            return jsonify({'result': output})
        else:
            return forbidden()


class ServiceApi(Resource):
    """
    Flask-resftul resource for returning db.meal collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add MealApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(MealApi, '/meal/<meal_id>')
    """
    @jwt_required()
    def get(self, service_name: str) -> Response:
        """
        GET response method for single documents in meal collection.
        :return: JSON object
        """
        output = Services.objects.get(service=service_name)
        return jsonify({'result': output})

    @jwt_required()
    def put(self, service_name: str) -> Response:
        """
        PUT response method for updating a meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            put_user = Services.objects(service=service_name).update(**data)
            output = {'service': str(put_user.service)}
            return jsonify({'result': output})
        else:
            return forbidden()
    

    @jwt_required()
    def delete(self, service_name: str) -> Response:
        """
        DELETE response method for deleting single meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """

        authorized: bool = Users.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Services.objects(service=service_name).delete()
            return jsonify({'result': output})
        else:
            return forbidden()




#Service in one specific direction: what are the platforms used?
class ServiceFlowsApi(Resource):
    @jwt_required()
    def get(self):
        output = ServiceFlows.objects()
        return jsonify({'result': output})


    @jwt_required()
    def post(self) -> Response:
        """
        POST response method for creating meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = ServiceFlows.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = ServiceFlows(**data).save()
            output = {'service': str(post_user.service), 'direction': str(post_user.direction)}
            return jsonify({'result': output})
        else:
            return forbidden()



class ServiceFlowApi(Resource):
    """
    Flask-resftul resource for returning db.meal collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add MealApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(MealApi, '/meal/<meal_id>')
    """
    @jwt_required()
    def get(self, service_name: str, direction: str) -> Response:
        """
        GET response method for single documents in meal collection.
        :return: JSON object
        """
        output = ServiceFlows.objects.get(service=service_name, direction=direction)
        return jsonify({'result': output})

    @jwt_required()
    def put(self, service_name: str, direction: str) -> Response:
        """
        PUT response method for updating a meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = ServiceFlows.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            put_user = ServiceFlows.objects(service=service_name, direction=direction).update(**data)
            return jsonify({'result': put_user})
        else:
            return forbidden()
    

    @jwt_required()
    def delete(self, service_name: str, direction: str) -> Response:
        """
        DELETE response method for deleting single meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = ServiceFlows.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = ServiceFlows.objects(service=service_name, direction=direction).delete()
            return jsonify({'result': output})
        else:
            return forbidden()



    
#Trains are specific instances of a directional service
class TrainsApi(Resource):
    @jwt_required()
    def get(self):
        output = Trains.objects()
        return jsonify({'result': output})


    @jwt_required()
    def post(self) -> Response:
        """
        POST response method for creating meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Trains.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            post_user = Trains(**data).save()
            output = {'train_number': str(post_user.train_number)}
            return jsonify({'result': output})
        else:
            return forbidden()



class TrainApi(Resource):
    """
    Flask-resftul resource for returning db.meal collection.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add MealApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(MealApi, '/meal/<meal_id>')
    """
    @jwt_required()
    def get(self, train_number: int) -> Response:
        """
        GET response method for single documents in meal collection.
        :return: JSON object
        """
        output = Trains.objects.get(train_number=train_number)
        return jsonify({'result': output})

    @jwt_required()
    def put(self, train_number: int) -> Response:
        """
        PUT response method for updating a meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        authorized: bool = Trains.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            data = request.get_json()
            put_user = Trains.objects(train_number=train_number).update(**data)
            return jsonify({'result': put_user})
        else:
            return forbidden()
    

    @jwt_required()
    def delete(self, train_number: int) -> Response:
        """
        DELETE response method for deleting single meal.
        JSON Web Token is required.
        Authorization is required: Access(admin=true)
        :return: JSON object
        """
        #authorized: bool = Meals.objects.get(id=get_jwt_identity()).access.admin

        authorized: bool = Trains.objects.get(id=get_jwt_identity()).access.admin

        if authorized:
            output = Trains.objects(train_number=train_number).delete()
            return jsonify({'result': output})
        else:
            return forbidden()
