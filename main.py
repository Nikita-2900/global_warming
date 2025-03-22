from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
app = Flask(__name__)

app.config.update(
    SECRET_KEY = 'WOW SUCH SECRET'
)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "products"

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(products):
    return User(products)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product1')
def product1():
    return render_template('product1.html')

@app.route('/product2')
def product2():
    return render_template('product2.html')

if __name__ == "__main__":
    app.run()

