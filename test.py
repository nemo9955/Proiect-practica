from flask import Flask
app = Flask(__name__)

# @app.route("/tudor")
# def tudor():
#     return "Ce mai faci epic"p

@app.route("/hello/<name>")
def hello_name(name):
    if name.endswith('a'):
        return "asd gf "+"Hello %s!" % name


# def hello_world():
#   return 'srtddthtdy e mai faci epic'
# app.add_url_rule('/pag','hello', hello_world)


    
app.run(host="0.0.0.0",port=8899,debug=True)
