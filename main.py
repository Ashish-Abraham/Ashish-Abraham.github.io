#portfolio
import requests
from flask import Flask, render_template, url_for, redirect

app= Flask(__name__)

@app.route('/')
def test_portfolio():
    return "<h1> Testing portfolio </h1>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True)