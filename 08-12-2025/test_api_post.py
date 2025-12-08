from flask import Flask, jsonify, request

app = Flask(__name__)

items=["Apple", "Banana", "Orange"]

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    item=data.get("item")
    items.append(item)
    return "POST EXECUTED"

if __name__ == "__main__":
    app.run(debug=True)