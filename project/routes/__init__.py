from flask import Blueprint, request, abort, jsonify
from project import services
from werkzeug.exceptions import HTTPException

blueprint = Blueprint('main_blueprint',
                      __name__,
                      template_folder='templates',
                      static_folder='static')

@blueprint.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return services.index(request), 200
    
    else:
        abort(405)
        
# It's possible to make separate errorhandlers for each error code.
@blueprint.app_errorhandler(HTTPException)
def errorhandler_http(e):
    return jsonify({ 'error': e.description }), e.code