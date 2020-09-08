from flask import *
from logic.processCourseUrl import processCourseUrl
from logic.horarios import generate
from os import urandom

app = Flask(__name__, static_url_path='') #tbd
app.secret_key = urandom(20)

MAX_COURSES = 6 #bounded by css stuff

#change session to save courses
@app.route("/", methods=['GET','POST'])
def main():
    if request.method == 'GET':
        session['counter'] = 0
        return render_template("index.html")

    else:
        return generate(list(map(lambda x: request.form[x],sorted(request.form.keys()))))

@app.route("/api/processUrl", methods=['POST',])
def processUrl():
    try:
        course = processCourseUrl(request.form.get('url'),session['counter'])
    except:
        return 'Not a valid url!', 500

    if course != "":
        session['counter'] += 1 #shitty code please ignore
        return course

    return 'Not a valid course!', 500

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
