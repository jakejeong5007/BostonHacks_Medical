import base
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/buttonClicked', methods=['POST'])
def handle_button_click_food():
    # You can access sent data using request.json, request.form, or request.data depending on the content type
    data = request.json
    print("Button Clicked with data:", data)
    
    # Process the data to process information
    response = recommend_food(data)
    return jsonify({"status": "success", "message": response})


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
