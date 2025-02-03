from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data (can be replaced with a database or other data source)
products = [
    {"id": 1, "name": "Laptop", "price": 999, "description": "High-performance laptop"},
    {"id": 2, "name": "Mouse", "price": 25, "description": "Wireless mouse"},
    {"id": 3, "name": "Keyboard", "price": 75, "description": "Ergonomic keyboard"},
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product_details(product_id):
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if product:
        return render_template("product_details.html", product=product)
    else:
        return "Product not found"  # Or redirect to a 404 page

@app.route("/search", methods=["GET"])  # Handle search queries
def search():
    query = request.args.get("q")  # Get the search query from the 'q' parameter
    results = []

    if query:  # If there's a search query
        for product in products:
            if query.lower() in product["name"].lower() or query.lower() in product["description"].lower():
                results.append(product)

    return render_template("search_results.html", query=query, results=results)



if __name__ == "__main__":
    app.run(port=8000, debug=True)  # debug=True for automatic reloading during development