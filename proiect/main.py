from flask import Flask ,redirect, url_for, request, render_template

from login import app_login

app = Flask(__name__)
app.register_blueprint(app_login)


server_port=8899
server_ip='http://192.168.56.101:'+ str(server_port)

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=server_port,debug=True)





