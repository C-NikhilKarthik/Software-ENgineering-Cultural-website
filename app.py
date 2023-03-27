from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/artists')
def artists():
    return render_template('artists.html')

# Define an API route to return data as JSON
@app.route('/api/data')
def api_data():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
