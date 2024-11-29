# from App import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

# class SoilAnalysis(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ph = db.Column(db.Float, nullable=False)
#     moisture = db.Column(db.Float, nullable=False)
#     soil_type = db.Column(db.String(50), nullable=False)
#     terrain_id = db.Column(db.Integer, db.ForeignKey('terrain.id'), nullable=False)

# class Terrain(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     area = db.Column(db.Float, nullable=False)  # Área do terreno em m²
#     latitude = db.Column(db.Float, nullable=False)
#     longitude = db.Column(db.Float, nullable=False)
#     soil_analyses = db.relationship('SoilAnalysis', backref='terrain', lazy=True)







# from app import db

# class SoilAnalysis(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     soil_type = db.Column(db.String(50), nullable=False)
#     suitability_score = db.Column(db.Float, nullable=False)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)











from . import db

class Terrain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.Float)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    soil_type = db.Column(db.String(50))
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<Terrain {self.id}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
