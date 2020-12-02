from app import app

@app.route('/') 
def index():
    return "Welcome to calculator"

@app.route('/add/<x>/<y>')
def add(x, y):
    return f'{int(x)}' + f'{int(y)}', add(x + y)