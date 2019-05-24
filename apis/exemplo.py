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

@api.route('/consulta')
class Fazer_consulta(Resource):
    @api.response(200, '{"status": "Ok"}')
    @api.response(400, '{"erro": "Tente novamente mais tarde"}')
    def get(self):
        '''Explicação específica deste endpoint.
        '''
        try:
            return dict(status = 'Ok'), 200
        except:
            return dict(erro = 'Tente novamente mais tarde')