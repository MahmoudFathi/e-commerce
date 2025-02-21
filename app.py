from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
products = [
    {"id": 1, "name": "Product 1", "price": 100},
    {"id": 2, "name": "Product 2", "price": 200},
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = next((prod for prod in products if prod["id"] == id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
