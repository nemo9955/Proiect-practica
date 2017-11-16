from flask import Flask ,redirect, url_for, request, render_template
from flask import Blueprint

app_login = Blueprint('app_login', __name__)

@app_login.route('/succes/<nume>/<pren>')
# @app_login.route('/succes/<nume>/')
# @app_login.route('/succes/<nume>')
def succes(nume,pren):
	return 'Bine ai venit %s %s' % (nume ,pren)



# @app_login.route('/login')
# def login_page():
#    return render_template('login.html')


# print '0000000000000000000000000000'

# print server_ip

@app_login.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		firstName = request.form['FirstName']
		lastName = request.form.get('LastName',' ')
		return redirect(url_for('succes',nume = firstName,pren=lastName))
	else:
		return render_template('login.html')

	  # firstName = request.args.get('FirstName')
	  # lastName = request.args.get('LastName',' ')
	  # return redirect(url_for('succes',nume = firstName,pren=lastName))

# if __name__ == '__main__':
# 	app_login.run(host="0.0.0.0",port=server_port,debug=True)