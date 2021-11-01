from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index_route():
    posts = process_images(read_data("./data/posts/posts.txt"), "posts")
    return render_template('public/index.html', post_list=posts)

@app.route('/officers')
@app.route('/officers.html')
def officer_page():
    officers = read_data("./data/officers/officers.txt")
    return render_template('public/officers.html', officer_list = officers)

@app.route('/events')
@app.route('/events.html')
def events_page():
    events = process_images(read_data("./data/events/events.txt"), "events")
    return render_template('public/events.html', event_list = events)

@app.route('/events/<target>')
@app.route('/events/<target>.html')
def event_page(target):
    metadata, subgroups = process_event(read_data("./data/events/" + target + ".txt"))
    return render_template('event.html', event_title = metadata['title'], event_list = subgroups)

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
        keyvals = [line.split(' //')[0].split(':', 1) for line in data.split('\n') if line.lstrip() != '' and line.split('//')[0]]
        ret_list.append({k: v.lstrip() for k, v in keyvals})
    return ret_list

def process_images(data, base_folder):
    for item in data:
        if 'image-folder' in item:
            item['images'] = ['img/' + base_folder + '/' + item['image-folder'] + '/' + img for img in sorted(os.listdir('./static/img/' + base_folder + '/' + item['image-folder'])) if img != '.DS_Store']
        if 'header-img' in item:
            item['header-img'] = 'img/'+ base_folder + '/' + item['image-folder'] + '/' + item['header-img']
        if 'subfolder' in item:
            item['images'] = ['img/' + base_folder + '/' + item['subfolder'] + '/' + img for img in sorted(os.listdir('./static/img/' + base_folder + '/' + item['subfolder'])) if img != '.DS_Store']
    return data

def process_event(data):
    metadata, subgroups = data[0], data[1:]
    print(metadata)
    process_images(subgroups, 'events/' + metadata['image-folder'])
    return metadata, subgroups

if __name__ == '__main__':
    app.run(debug=True)
