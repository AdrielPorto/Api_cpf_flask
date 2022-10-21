import re
from flask import request
from flask_restful import Resource
from application.server import api
from application.routes.utils import HTTP_STATUS_CODE
from application.routes.utils import get_json, get_from_request


class CPF(Resource):
    def post(self):
        try:
            data = get_json(request)

            cpf = get_from_request(data, 'cpf')
            cpf = re.sub('[^0-9]', '', cpf)

        except Exception as e:
            resp = {
                    'error': str(e),
                    'status': HTTP_STATUS_CODE['BAD_REQUEST']
            }

            return resp

        is_valid = self.valida_cpf(cpf)

        resp = {
                'is_valid': is_valid,
                'status': HTTP_STATUS_CODE['OK']
        }

        return resp

    def valida_cpf(self, cpf):
        is_valid = True

        if len(cpf) != 11 or cpf.count(cpf[0]) == 11:
            is_valid = False

        if(is_valid):
            is_valid = self._valida_digito(cpf, -2, 10)

        if(is_valid):
            is_valid = self._valida_digito(cpf, -1, 11)

        return is_valid

    def _valida_digito(self, cpf, pos, count):
        digito_valido = True

        soma = [int(a)*b for a, b in zip(cpf[:pos], range(count, 1, -1))]
        soma = 10*sum(soma)

        if soma % 11 != int(cpf[pos]):
            digito_valido = False

        return digito_valido


def init_routes():
    api.add_resource(CPF, '/validar/cpf')

