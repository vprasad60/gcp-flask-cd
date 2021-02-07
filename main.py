# Import libraries
from flask import Flask
from flask import request
import datetime

# Initialize app
app = Flask(__name__)

# Basic app route
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

# Return day of the week for any date
@app.route('/date/')
def find_day():
    # Find today's date
    today = datetime.datetime.today().strftime('%m-%d-%Y')
    # Accept an input for a date, otherwise use today's date
    date = request.args.get('date', today)

    # Find day of the week for the inputted date (or today's date)
    if date:
        day = datetime.datetime.strptime(date, '%m-%d-%Y').strftime('%A')
    else:
        day = datetime.datetime.strptime(today, '%m-%d-%Y').strftime('%A')

    # Return day of the week
    return (
    """<form action="" method="get">
            Input a date in the following format: MM-DD-YYYY <br><br>
            Date: <input type="text" name="date">
            <input type="submit" value="Find Day of the Week">
        </form>"""
    + day
)
  
# Run app on local host
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
