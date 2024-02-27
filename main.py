from flask import Flask, render_template, request
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
socketio = SocketIO(app)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)
        create = request.form.get('create', False)

        if not name:
            return render_template('home.html', error='Please enter a name.')

        if join and not code:
            return render_template('home.html', error='Please enter a code.')

    return render_template('home.html')


if __name__ == "__main__":
    socketio.run(app, debug=True)