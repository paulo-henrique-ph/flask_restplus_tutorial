import json
from flask_restplus import Namespace, Resource, fields
from flask import request
from core import Classe_exemplo

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

@api.route('/consulta/<string:nome>')
class Fazer_consulta_com_param(Resource):
    @api.param('nome','O nome da pessoa')
    @api.response(200, '{"status": "Ip público"}')
    @api.response(400, '{"erro": "Não conseguimos nos conectar"}')
    def get(self, nome):
        '''Explicação específica deste endpoint.
        '''
        try:
            controlador = Classe_exemplo()
            response, status = controlador.consulta_com_nome()
            if status:
                return dict(status = response), 200
            
            return dict(erro = response)
        except:
            return dict(erro = 'Tente novamente mais tarde')