#portfolio

from flask import Flask, render_template, url_for, redirect

app= Flask(__name__)

@app.route('/')
@app.route('/about')
@app.route('/contact')
@app.route('/projects')
@app.route('/blog')

if __name__ == "__main__":
    app.run(debug=True)