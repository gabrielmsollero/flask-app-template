from flask import Request, render_template, abort

def index(request: Request):
    try:
        return render_template('template.html', variable='testvar')
    
    except Exception as e:
        abort(e.code, description=e.description)