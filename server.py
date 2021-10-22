from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index_route():
    posts = process_index(read_data("./data/posts/posts.txt"))
    return render_template('public/index.html', post_list=posts)

@app.route('/officers')
@app.route('/officers.html')
def officer_page():
    officers = read_data("./data/officers/officers.txt")
    return render_template('public/officers.html', officer_list = officers)

@app.route('/<target>')
@app.route('/<target>.html')
def nav_target_route(target):
    return render_template('public/' + target+'.html')


def read_data(filepath):
    f = open(filepath, "r")
    raw = f.read()
    f.close()
    curr_data = raw.split('===')[0]
    indiv_data = curr_data.split('---')
    ret_list = []
    for data in indiv_data:
        # TODO: Add escaping // ? maybe with regex.
        keyvals = [line.split(' //')[0].split(':', 1) for line in data.split('\n') if line != '' and line.split('//')[0]]
        ret_list.append({k: v.lstrip() for k, v in keyvals})
    return ret_list

def process_index(index_data):
    for post in index_data:
        if 'image-folder' in post:
            post['image-folder'] = "".join(post['image-folder'].split())
            post['images'] = ['img/' + post['image-folder'] + '/' + img for img in sorted(os.listdir('./static/img/' + post['image-folder'])) if img != '.DS_Store']
    return index_data

if __name__ == '__main__':
    app.run(debug=True)
