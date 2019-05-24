import json
from flask_restplus import Namespace, Resource, fields
from flask import request

api = Namespace('Exemplo',
    description = 'Este é um exemplo de API'
)

# modelo de JSON a ser seguido
exemplo_modelo = api.model('Exemplo', {
    'nome': fields.String(
        required = True,
        description = 'Nome da pessoa'
    )
})