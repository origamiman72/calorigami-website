from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index_route():
    print('posts', announcement)
    return render_template('/index.html', announcement=announcement, post_list=posts)

@app.route('/<target>')
@app.route('/<target>.html')
def nav_target_route(target):
    implemented_elsewhere=['officers', 'index']
    if target not in implemented_elsewhere:
        return render_template(target+'.html')
    return None

@app.route('/officers')
@app.route('/officers.html')
def officer_page():
    return render_template('/officers.html', officer_list = officers)

def read_data(filepath):
    f = open(filepath, "r")
    raw = f.read()
    f.close()
    curr_data = raw.split('===')[0]
    indiv_data = curr_data.split('---')
    ret_list = []
    for data in indiv_data:
        keyvals = [line.split(':') for line in data.split('\n') if line != '']
        ret_list.append({k: v for k, v in keyvals})
    return ret_list

def process_index(index_data):
    global announcement
    global posts
    announcement = index_data[0]['announcement']
    posts = index_data[1:]
    for post in posts:
        post['image-folder'] = "".join(post['image-folder'].split())
        post['images'] = []
        post['images'] = ['img/' + post['image-folder'] + '/' + img for img in os.listdir('./static/img/' + post['image-folder'])]
        print(post['images'])

if __name__ == '__main__':
    global officers
    global index_data
    officers = read_data("./data/officers/officers.txt")
    process_index(read_data("./data/posts/posts.txt"))
    app.run()