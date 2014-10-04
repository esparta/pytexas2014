from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for
from flask import redirect, render_template, abort 

app = Flask(__name__)
 
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
app = Flask(__name__)

from models import Entidad, Municipio

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return redirect(url_for("entidad", cve_ent=request.form["cve_ent"]))

    entidades = Entidad.query.all()
    return render_template("index.html", msg='Open Data Sample', title='Home',
                           entidades=entidades)

@app.route('/entidad/<cve_ent>')
def entidad(cve_ent):
    entidad = Entidad.query.get(cve_ent)
    return render_template("view.html", title='Listado de entidades', entidad=entidad)


from api import api, EntidadList, EntidadAPI

api.add_resource(EntidadList, '/api/v1.0/entidad/')
api.add_resource(EntidadAPI, '/api/v1.0/entidad/<cve_ent>')


if __name__ == '__main__':
    app.run()
