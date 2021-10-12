# project resources
from models.services import Services
from tools.mongo_loader import mongo

# external packages
import csv


@mongo
def csv_to_service(filepath: str = 'resources/service_data.csv', delimiter: str = ','):
    """
    Converts data in csv file to documents in meal collection.
    Uses @mongo wrapper to connect via mongoengine during execution.
    :param filepath:
    :param delimiter:
    :return:
    """
    print("ok")
    with open(filepath, 'r') as file:
        data = csv.DictReader(file, delimiter=delimiter)
        for datum in data:
            service_n = datum['service']
            if len(Services.objects(service=service_n))>0: continue
            line = Services(**datum, __auto_convert=True).save()
            print(f"Added: {line.service} | {line.operator} | {line.tph} => {line.service}")




def load_all(config: dict = None):
    """
    Load test data into given configuration.
    :return:
    """
    from tools.mongo_loader import default_config

    if config:
        default_config.update(config)

    csv_to_service()
