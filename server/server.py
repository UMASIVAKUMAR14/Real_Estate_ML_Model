from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_house_price', methods = ['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    area_type = request.form['area_type']
    bed = int(request.form['bed'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    
    response = jsonify({
        'estimated_price' : util.get_estimated_price(location, area_type, total_sqft, bath, balcony, bed)
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print ("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
