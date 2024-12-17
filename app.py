from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load product data
def load_product_data():
    with open('data/product_data.json') as f:
        return json.load(f)['products']

# Load featured products
def load_featured_products():
    with open('data/featured.json') as f:
        return json.load(f)['featured']

@app.route('/')
def home():
    featured_products = load_featured_products()
    return render_template('home.jinja', featured=featured_products)

@app.route('/products')
def products():
    all_products = load_product_data()
    return render_template('product_page.jinja', products=all_products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    all_products = load_product_data()  # Load all products from the JSON file
    product = next((p for p in all_products if p['id'] == product_id), None)  # Find the product by ID
    if product is None:
        return "Product not found", 404  # Handle case where the product does not exist
    return render_template('product_detail.jinja', product=product)  # Render the product detail page with the product data

@app.route('/lookbook')
def lookbook():
    # Placeholder for lookbook page
    return render_template('lookbook.jinja')

@app.route('/archive')
def archive():
    # Placeholder for archive page
    return render_template('archive.jinja')

@app.route('/about')
def about():
    # Placeholder for about page
    return render_template('about.jinja')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle the form submission logic here (e.g., sending an email, saving data to the database)
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # For now, you can print it to the console
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return render_template('contact.jinja', success=True)  # You can pass success=True to show a success message.
    return render_template('contact.jinja')  # Render the contact page initially

if __name__ == '__main__':
    app.run(debug=True)
