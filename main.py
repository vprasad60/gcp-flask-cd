# Import libraries
from flask import Flask
from flask import jsonify
import wikipedia

# Initialize app
app = Flask(__name__)

# Basic app route
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

# Show name in JSON format
@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

# Display first 10 sentences of Wikipedia article 
@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=10)
    return result

# Run app on local host
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
