from flask import Flask, render_template, request, url_for
app = Flask(__name__)


# debug = True

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(
    	debug=True
    )



# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
# @app.route('/hello/', methods=['POST'])
# def hello():
#     name=request.form['yourname']
#     email=request.form['youremail']
#     return render_template('form_action.html', name=name, email=email)

