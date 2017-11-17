from flask import Flask ,redirect, url_for, request, render_template
from flask import Blueprint

import json

app_login = Blueprint('app_login', __name__)

@app_login.route('/succes/<idd>')
# @app_login.route('/succes/<nume>/')
# @app_login.route('/succes/<nume>')
def succes(idd): # IDul e acelasi ca email-ul
	print 'Bine ai venit %s ' % ( json.dumps(bazadate,indent=4) )
	if idd in bazadate:
		return render_template('test.html', user = bazadate[idd])
	else:
		return 'Userul nu existe!'



# @app_login.route('/login')
# def login_page():
#    return render_template('login.html')


# print '0000000000000000000000000000'

# print server_ip


bazadate = {
	"Tudor": {
		"LastName": "Pop",
		"pwd": "1234",
		"FirstName": "Tudor",
		"Mail": "Tudor"
	},
	"Andrei": {
		"LastName": "Costache",
		"pwd": "0000",
		"FirstName": "Andrei",
		"Mail": "Andrei"
	},
	"George": {
		"LastName": "Milos",
		"pwd": "1111",
		"FirstName": "George",
		"Mail": "George"
	}
}


@app_login.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		firstName = request.form['FirstName']
		lastName = request.form.get('LastName', None)
		password= request.form.get('pwd')
		mail=request.form.get('Mail')

		if mail in bazadate:

			if password == bazadate[mail]['pwd'] :
				return redirect(url_for('app_login.succes',idd = mail))
			else:
				return 'Parola gresita!'

		else:
			bazadate[mail]={}
			usr=bazadate[mail]
			usr['FirstName'] = firstName
			usr['LastName'] = lastName
			usr['Mail'] = mail
			bazadate[mail]['pwd'] = password
			return redirect(url_for('app_login.succes',idd = mail))


	else:
		return render_template('login.html')

	  # firstName = request.args.get('FirstName')
	  # lastName = request.args.get('LastName',' ')
	  # return redirect(url_for('succes',nume = firstName,pren=lastName))

# if __name__ == '__main__':
# 	app_login.run(host="0.0.0.0",port=server_port,debug=True)