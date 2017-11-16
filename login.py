from flask import Flask ,redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/succes/<nume>/<pren>')
# @app.route('/succes/<nume>/')
# @app.route('/succes/<nume>')
def succes(nume,pren):
	return 'Bine ai venit %s %s' % (nume ,pren)

server_port=8899
server_ip='http://192.168.56.101:'+ str(server_port)

print server_ip

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      firstName = request.form['FirstName']
      lastName = request.form.get('LastName',' ')
      return redirect(url_for('succes',nume = firstName,pren=lastName))
   else:
      firstName = request.args.get('FirstName')
      lastName = request.args.get('LastName',' ')
      return redirect(url_for('succes',nume = firstName,pren=lastName))



def cevaprint(asd='X'):
	print 'aaaaaaaaaaaaaaaaaaaa',asd
	return 4

print __name__, 'login.py'

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=server_port,debug=True)