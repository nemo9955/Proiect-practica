from flask import Flask ,redirect, url_for, request, render_template
from flask_socketio import SocketIO, emit
import random, threading

from login import app_login


server_port=8899
server_ip='http://192.168.56.101:'+ str(server_port)

app = Flask(__name__)
app.register_blueprint(app_login)
app.config['SECRET_KEY'] = 'secvbrdfgfdgdfet!'
# app.config['PORT'] = server_port
# app.config['DEBUG'] = True
socketio = SocketIO(app)


@app.route('/')
def index():
	return "Hello,  World!"



@socketio.on('my event', namespace='/test')
def test_message(message):
	emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
	emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
	emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print('Client  disconnected')


if __name__ == '__main__':
	# t = threading.Thread(target=serverWS)
	# t.daemon = True
	# t.start()
	# print 'pornim server HTTP'
	app.run(host="0.0.0.0",port=server_port,debug=True)
	# socketio.run(app,host="0.0.0.0",port=server_port,debug=True, use_reloader=False)


