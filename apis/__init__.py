from flask_restplus import Api
from .exemplo import api as exemplo

api = Api(
    title='',
    version='1.0',
    description=''
    # API metadatas
)

api.add_namespace(exemplo)