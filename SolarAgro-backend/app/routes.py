# from flask import Blueprint, render_template, request, jsonify
# from App import db
# from App.models import Terrain, SoilAnalysis
# from App.controllers import calcular_viabilidade, estimar_producao_energia
# from App.utils import gerar_relatorio_pdf

# bp = Blueprint('api', __name__)


# @bp.route('/api/viabilidade', methods=['POST'])
# def viabilidade():
#     data = request.get_json()
#     resultado = calcular_viabilidade(data)
#     return jsonify({'viabilidade': resultado})

# @bp.route('/api/energia', methods=['POST'])
# def energia():
#     data = request.get_json()
#     producao = estimar_producao_energia(data['area'])
#     return jsonify({'energia_estimativa': producao})

# @bp.route('/api/relatorio', methods=['POST'])
# def relatorio():
#     data = request.get_json()
#     relatorio_path = gerar_relatorio_pdf(data)
#     return jsonify({'relatorio': relatorio_path})


# @bp.route('/')
# def index():
#     return render_template('index.html')

# @bp.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @bp.route('/terreno/<int:id>')
# def terreno(id):
#     terrain = Terrain.query.get(id)
#     return render_template('terreno.html', terrain=terrain)









# from flask import Blueprint, render_template

# api = Blueprint('api', __name__)

# # Página inicial
# @api.route('/')
# def index():
#     return render_template('index.html')

# # Página do dashboard
# @api.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# # Página de detalhes do terreno
# @api.route('/terreno/<int:id>')
# def terreno(id):
#     # Simulação de dados de terreno (você pode integrar ao banco de dados aqui)
#     terrain = {
#         "id": id,
#         "area": 5000,
#         "latitude": -15.7801,
#         "longitude": -47.9292
#     }
#     return render_template('terreno.html', terrain=terrain)










# app/routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Terrain

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/dashboard')
def dashboard():
    terrenos = Terrain.query.all()  # Pega todos os terrenos do banco
    return render_template('dashboard.html', terrenos=terrenos)

@bp.route('/adicionar_terreno', methods=['GET', 'POST'])
def adicionar_terreno():
    if request.method == 'POST':
        area = request.form['area']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        soil_type = request.form['soil_type']
        description = request.form['description']
        novo_terreno = Terrain(area=area, latitude=latitude, longitude=longitude, soil_type=soil_type, description=description)
        db.session.add(novo_terreno)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('adicionar_terreno.html')

@bp.route('/terreno/<int:id>')
def terreno(id):
    terrain = Terrain.query.get(id)  # Obtém um terreno pelo ID
    return render_template('terreno.html', terrain=terrain)
