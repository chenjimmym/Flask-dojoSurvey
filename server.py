from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'aSecret'

@app.route('/')
def mainPage():
    return render_template('index.html')

@app.route('/name', methods=['POST'])
def showSubmitted():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(name) > 0 and len(name) < 121 and len(comment) > 0 and len(comment) < 121:
        return render_template('result.html', name = name, location = location, language = language, comment = comment)
    if len(name) < 1:
        flash("Name cannot be empty!")
    elif len(name) > 120:
        flash("Name cannot be long than 120 characters.")
    if len(comment) < 1:
        flash("Comment cannot be empty!")
    elif len(comment) > 120:
        flash("Comment cannot be long than 120 characters.")
    return redirect('/')

app.run(debug=True)