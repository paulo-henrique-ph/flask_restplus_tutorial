import json
from flask_restplus import Namespace, Resource, fields
from flask import request
from core import ClasseExemplo


api = Namespace(
    'Exemplo',
    description='Este é um exemplo de API'
)

# modelo de JSON a ser seguido
exemplo_modelo = api.model(
    'Exemplo',
    {
        'nome': fields.String(
            required=True,
            description='Nome da pessoa'
        )
    }
)


@api.route('/consulta')
class FazerConsulta(Resource):
    @api.response(200, '{"status": "Ok"}')
    @api.response(500, '{"erro": "Tente novamente mais tarde"}')
    def get(self):
        '''Explicação específica deste endpoint.
        '''
        try:
            return dict(status='Ok'), 200
        except Exception as e:
            return dict(
                erro='Tente novamente mais tarde',
                mensagem=e
            ), 500


@api.route('/consulta/<string:nome>')
class FazerConsultaComParam(Resource):
    @api.param('nome', 'O nome da pessoa')
    @api.response(200, '{"status": "Ip público"}')
    @api.response(400, '{"erro": "Não conseguimos nos conectar"}')
    def get(self, nome):
        '''Explicação específica deste endpoint.
        '''
        try:
            controlador = Classe_exemplo()
            response, status = controlador.consulta_com_nome()
            if status:
                return dict(status=response), 200

            return dict(erro=response)
        except Exception as e:
            return dict(
                erro='Tente novamente mais tarde',
                mensagem=e
            ), 500


@api.route('/enviar_dados')
class EnviarDados(Resource):
    @api.expect(exemplo_modelo)
    @api.response(200, '{"status": "Ok"}')
    @api.response(500, '{"erro": "Tente novamente mais tarde"}')
    @api.response(400, '{"erro": "requisição inválida"}')
    def post(self):
        try:
            if request.is_json and len(request.data) > 0:
                req = request.get_json()
                print(req)
                return dict(status='Ok'), 200

            return dict(erro='requisição inválida'), 400
        except Exception as e:
            return dict(
                erro='Tente novamente mais tarde',
                mensagem=e
            ), 500
