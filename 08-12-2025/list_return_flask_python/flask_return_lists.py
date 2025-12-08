from flask import Flask, jsonify

app=Flask(__name__)

items=['Apple', 'banana', 'Mango']

@app.route('/items', methods=["GET"])
def get_items():
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)