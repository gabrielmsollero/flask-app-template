from flask import Flask 
import os

def create_app():
    app = Flask(__name__)
    
    config_type = os.getenv('CONFIG_TYPE', default='settings.DevelopmentConfig')
    app.config.from_object(config_type)
    
    print(app.config)
    
    from project.routes import blueprint
    app.register_blueprint(blueprint ,url_prefix="/")

    return app