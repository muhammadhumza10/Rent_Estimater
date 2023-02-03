from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_city_names', methods=['GET'])
def get_city_names():
    response = jsonify({
        'city': util.get_city_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response








@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    area_sqft = float(request.form['area_sqft'])
    location = request.form['location']
    city = request.form['city']
    bedrooms = int(request.form['bedrooms'])
    baths = int(request.form['baths'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(city,location,area_sqft,bedrooms,baths)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()












