from flask import Flask ,redirect, url_for, request, render_template
app = Flask(__name__)

# #1
# @app.route("/tudor")
# def tudor():
# 	return "Ce mai faci coleredirect, url_forgu"

# #3
# @app.route("/hello/<name>")
# def hello_name(name):
# 	if name.lower().endswith('a'):
# 		return "Buna draga mea  %s" % name + ', iti urez o zi frumoasa!'
# 	else:
# 		return "Ceau %s" % name +' , cum mai merge cu serialele?'

# #2
# def hello_world():
#   return 'srtddthtdy e mai faci epic'
# app.add_url_rule('/pag','hello', hello_world)

# #4
# @app.route('/blog/<int:numar>')
# def show_blog(numar):
#    return 'Numarul ales este  %d' % numar

# #5
# @app.route('/rev/<float:virgula>')
# def revision(virgula):
# 	print type(virgula)
# 	print virgula
# 	return 'Numarul ales este  %f' % virgula

# #6
# @app.route('/admin')
# def hello_admin():
#    return 'Hello Admin'

# #7
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest

# #8
# @app.route('/user/<tip>')
# def hello_user(tip):
#    if tip =='admin':
# 	  return redirect(url_for('hello_admin'))
#    else:
# 	  return redirect(url_for('hello_guest',guest = tip))


@app.route('/succes/<nume>/<pren>')
@app.route('/succes/<nume>/')
@app.route('/succes/<nume>')
def succes(nume,pren=' '):
	return 'Bine ai venit %s %s' % (nume ,pren)


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



# @app.route('/')
# def index():
#    return '<html><body><h3>  Hello World  </h3></body></html>'

# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('index.html', name = user)

# @app.route('/hello/<int:score>')
# def hello_name(score):
#    return render_template('index.html', marks = score)

# @app.route('/result')
# def result():
#    dict = {'phy':50,'che':60,'maths':70}
#    return render_template('index.html', result = dict)

# @app.route("/")
# def index():
#    return render_template("index.html")

import login
# import prob
print __name__, 'test.py'
print login.cevaprint('CV')

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=8899,debug=True)