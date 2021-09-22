from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_route():
    return render_template('/index.html')

@app.route('/<target>')
@app.route('/<target>.html')
def nav_target_route(target):
    return render_template(target+'.html')

if __name__ == '__main__':
    app.run()