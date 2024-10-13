from flask import Flask, jsonify
# print(dir(flask))

# Step 1 :- Create a flask application instance
app = Flask(__name__)

# Step 2 :- Define a route for the API(Application Programming Interface)
@app.route('/api/hello', methods=['GET'])
def hello():
    # Step 3 :- Define the data to return when this route is accessed
    response = {
        'Message' : 'Hello World!',
        'Status' : 'Success'
    }
    
    # Step 4 :- Return the data in JSON response
    return jsonify(response)

# Step 5 :- Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
