from flask import Flask, request, jsonify
import model2
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/get_recommendations', methods=['GET', 'POST'])
def get_recommendations():
    if request.method == 'POST':
        data = request.json
        movie_name = data.get('movie')
        recommendations = model2.recommedate(movie_name)
        response = jsonify(recommendations)
        print(response.json)  # Print the JSON data within the response to the Flask console
        return response
    elif request.method == 'GET':
        # Handle the GET request (if needed) or return an appropriate response
        data = request.args
        movie_name = data.get('movie')
        recommendations = model2.recommedate(movie_name)
        response = jsonify(recommendations)

        return response

      
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)# using this we can access the api from any ip address but it is not required in this case as we are using it locally


# from flask import Flask, request, jsonify
# import model

# app = Flask(__name__)

# @app.route('/get_recommendations', methods=['GET', 'POST'])
# def get_recommendations():
#     if request.method == 'POST':
#         data = request.json
#         movie_name = data.get('movie')
#         recommendations = model.recommedate(movie_name)
#         response = jsonify(recommendations)
#         print(response.json)  # Print the JSON data within the response to the Flask console
#         return response
#     elif request.method == 'GET':
#         movie_name = request.args.get('movie')
#         recommendations = model.recommedate(movie_name)
#         response = jsonify(recommendations)
#         print(response.json)  # Print the JSON data within the response to the Flask console
#         return response

# if __name__ == '__main__':
#     app.run()
