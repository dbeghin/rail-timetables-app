# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.user import UsersApi, UserApi
from api.productionplan import ProductionPlanApi
from api.service import ServicesApi, ServiceApi, ServiceFlowsApi, ServiceFlowApi, TrainsApi, TrainApi
from api.connection import NodeConnectionsApi, NodeConnectionApi, ConflictsApi, ConflictApi


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    :Example:
        api.add_resource(HelloWorld, '/', '/hello')
        api.add_resource(Foo, '/foo', endpoint="foo")
        api.add_resource(FooSpecial, '/special/foo', endpoint="foo")
    """
    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')

    api.add_resource(ProductionPlanApi, '/productionplan')
    
    api.add_resource(ServicesApi, '/service/')
    api.add_resource(ServiceApi, '/service/<service_name>')
    
    api.add_resource(ServiceFlowsApi, '/route/')
    api.add_resource(ServiceFlowApi, '/route/<service_name>/<direction>')
    
    api.add_resource(TrainsApi, '/train/')
    api.add_resource(TrainApi, '/train/<train_number>')
    
    api.add_resource(NodeConnectionsApi, '/connection/')
    api.add_resource(NodeConnectionApi, '/connection/<connection_id>')
    
    api.add_resource(ConflictsApi, '/conflict/')
    api.add_resource(ConflictApi, '/conflict/<conflict_id>')
