from od import db

class Entidad(db.Model):
    __tablename__ = 'entidades'

    cve_ent = db.Column(db.String(2), primary_key=True)
    nom_ent = db.Column(db.String(50))
    nom_abr = db.Column(db.String(5))

    def __repr__(self):
        return "<Entidad(cve_ent='{self.cve_ent}', nombre='{self.nom_ent}')>".format(self=self)

class Municipio(db.Model):
    __tablename__ = 'municipios'

    cve_ent = db.Column(db.String(2), db.ForeignKey("entidades.cve_ent"), primary_key=True)
    nom_ent = db.Column(db.String(50))
    nom_abr = db.Column(db.String(5))
    cve_mun = db.Column(db.String(3), primary_key=True)
    nom_mun = db.Column(db.String(100))
    cve_cab = db.Column(db.String(4))
    nom_cab = db.Column(db.String(100))
    ptot = db.Column(db.Integer)
    pmas = db.Column(db.Integer)
    pfem = db.Column(db.Integer)
    vtot = db.Column(db.Integer)

    entidad = db.relationship("Entidad", backref=db.backref('municipios',
                                                   order_by=cve_mun))

    def __repr__(self):
        return "<Municipio(cve_mun='{self.cve_mun}', nombre='{self.nom_mun}'".format(self=self)
