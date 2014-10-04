from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal, marshal_with

from od import app
from models import Entidad, Municipio

api = Api(app)

entidad_fields = {
    'cve_ent':   fields.String,
    'nom_ent':    fields.String
}

class EntidadList(Resource):
    @marshal_with(entidad_fields)
    def get(self):
        return Entidad.query.all()

municipio_fields = {
    'cve_ent': fields.String,
    'cve_mun': fields.String,
    'nom_mun': fields.String,
    'ptot': fields.Integer,
    'pmas': fields.Integer,
    'pfem': fields.Integer,
}

class EntidadAPI(Resource):
    def get(self, cve_ent):
        entidad = Entidad.query.get(cve_ent)
        if not entidad:
            abort(404)
        return {'entidad': marshal(entidad, entidad_fields),
                'municipios': marshal(entidad.municipios, municipio_fields) }
