# [calorigami.berkeley.edu](https://calorigami.berkeley.edu)

## Update:

The website is currently being updated to use the Flask templating system more
extensively and being redesigned to make it easier to edit by future webmasters. New information
should be placed in `/data/` and will be automatically updated on the website.

### Pages currently using new templates:

- `templates/public/officers.html`
- `templates/public/index.html`
- `templates/public/events.html`
- `templates/event.html`

## Quick Start Guide

You must have installed:

- python3
- Flask
- git

To install, run

```bash
pip3 install flask --user
```

First, you must clone the repository:

```bash
git clone https://github.com/origamiman72/calorigami-website.git
```

To run the website server, run

```bash
python3 server.py
```

and navigate to `http://127.0.0.1:5000` in your browser to view the site.

To update the website, navigate to the relevant folder in `/data/` and update
using this format:

```
key1: value1
key2: value2
key3: value3
// etc

---
// The three dashes separate content, e.g. separate posts, officers, etc.

key1: value1
// etc

===
// Anything below the equals signs is ignored, can use for older information
```

As an example, for an officer, `/data/officers/officers.txt` should look like

```
name: Oski Bear
position: President
year: 4th
major: EECS
other: Likes python (the snake)

---

name: Carol Christ
//etc
```

Once all edits have been made, add and commit all changed files using git and push them to Github. You can then ssh into the OCF servers and run `./update.sh` to make your changes public.

```bash
# In your terminal
# Add all changed files
git add data/posts/posts.txt
# Save/Commit your changes with a descriptive message
git commit -m "Updated posts.txt"
# Push your changes to github
git push origin main

# On OCF servers
./update.sh
```

## New Posts

The posts file, located at `/data/posts/posts.txt`, controls the posts and announcements that show up on the homepage.

To make a new post, you must specify the type and give it a title and description.
There are two types of posts: `announcement` and `post`. Announcements are colored by the accent color to stand out while Posts are simply white with black/grey text.

```
// New Announcement Post

title: Meeting next week!
type: announcement
description: We are meeting next week at 7pm.

---

// New Meeting Post

title: 1/1/01 Meeting
type: post
description: Today we folded paper!
```

To add images to a post or announcement, create a folder under `/static/img/posts` and place your images within it. Then, place the folder name under the key `image-folder`.

e.g. for `/static/img/posts/meeting-1-1-01/<images>`, `/data/posts/posts.txt` should look like

```
---

title: 1/1/01 Meeting
type: post
description: We folded paper!
image-folder: meeting-1-1-01

---
```

### Advanced

The templating system supports inline html. As such, to bold text simply surround it with a `<strong>` tag, and to italicize surround it with an `<em>` tag. To link to a website, surround it with an `<a>` tag.

```html
description: This text is <strong>bold</strong>. This is in <em>italics</em>.
This is a <a href="https://ocf.io">link</a>.
```

If you would like to add custom styles to a post, add an `id` key/value. You can then target the post in `static/styles/scss/index.scss` using the new id value.

```css
// data/posts/posts.txt
title: 1/01/01 Meeting
type: post
description: We folded paper!
id: first-meeting-post

// static/styles/scss/index.scss
#first-meeting-post {
  color: blue;
  // etc
}
```

#### Custom Post

If you would like to create your own html for a post instead of using the default templates, you can do so by specifying an `html` key/value with the name of an html file for the new post. A template has been provided in `templates/custom_post_template.html` with more detailed instructions.

```
---

html: custom_post.html // This will render templates/custom_post.html instead of the default post

---
```

## Add Events

The file that controls the [events](https://calorigami.berkeley.edu/events) page is stored at `/data/events/events.txt`.
The template for a new event/year is as follows:

```
title: 2018-2019
image-folder: events-2018-2019
// The image, in image-folder, to be used as the image for the event card
header-img: giant-crane/tiredlam.jpg
// The path for the new event page (e.g. https://calorigami.berkeley.edu/2018-2019)
link: 2018-2019
```

When adding a new event, add a new entry in `events.txt` and add a new text file under `/data/events` for the new event.
The name of the text file **must match the `link` key for the event in `events.txt`**.

Inside the new file, you can define individual events/subheadings as such.

```
// data/events/2018-2019.txt
title: Events 2018-2019
image-folder: events-2018-2019

---

subheading: Life-Sized Humanoid Crane
description: For Cal Day 2019, Cal Origami folded a humanoid crane out of a 12 by 12 foot piece of paper!
// Folder inside image-folder with images of this specific event
subfolder: giant-crane

---

subheading: // etc

```

## Add/edit Officers

The file that controls the [officers](https://calorigami.berkeley.edu/officers) is stored at `/data/officers/officers.txt`
The template for a new officer is as follows:

```
---

name: Oski
position: President
year: 100th
major: Undeclared
other: Go Bears

---
```

## Other Information

All scss files should be compiled into the `/static/styles` folder. All html files in `templates/public` are accessible publicly by visiting `calorigami.berkeley.edu/file.html`.

## Background / Original README:

The Cal Origami website used to be hosted on weebly [calorigami.weebly.com/] and
when the staff decided to move it to the current site [calorigami.berkeley.edu]
they just saved the html from each weebly page. This resulted in a website with
pretty messy code, had lots of unneeded weebly trackers/stylesheets/whatever,
and was incredibly static (e.g. if you wanted to change the navbar, you'd
have to edit every single page). Copying the files in this way was effective for
migrating the site from weebly to berkeley.edu, but it meant that it would be
hard to edit the site.

I (Kai) put in a bit of work to migrate the website to the pretty popular Flask
web framework. I've also cleaned up a bit by ripping out some old weebly code.
The site is now pretty much identical as before, but it should be easier to add
new pages. It's now possible to change the navbar or footer in one place, and
have it affect all the pages.

To current and future webmasters: it's not really my place to make the design
choices for the site, that's up to you. I only chose to migrate to Flask because
I felt that it would be difficult to make the necessary changes in preparation
for EBOC, using the old weebly code. So if you have a revamp for the site in
mind, and you can best accomplish it by serving static pages or using another
framework, go for it.

Useful Links:
Flask documentation
[http://flask.pocoo.org/]
OCF+Flask Guide (they also have guides for Rails, Django, etc)
[https://www.ocf.berkeley.edu/docs/services/web/flask/]

A couple important things:

I. All old files are saved in ~/public_html.Backup.Fri-Jul-26-10:06:42-PST-2016
II. This Flask environment is set up so that any page in the templates directory
"/templates/abc.html" can be reached via either
"https://calorigami.berkeley.edu/abc"
or
"https://calorigami.berkeley.edu/abc.html".

    The only exception is layout.html, which only contains the navbar, header
    image, and footer.

III. See /templates/TEMPLATE.html for the general structure of a page.

IV. Image paths.
a. The folder that used to be /uploads/6/5/4/7/6547949/ got collapsed into
/static/uploads/ because they were unnecessarily nested (prob by weebly).
b. Flask code for referencing an image at /static/img/abc.jpg:
{{url_for('static', filename='img/abc.jpg')}}
For example:
<img src="{{url_for('static', filename='img/abc.JPG')}}" />
<a href="{{url_for('static', filename='img/abc.jpg')}}">Link</a>

V. If you make some changes & the site didn't update, try this command over ssh:
$ touch ~/public_html/run.fcgi
Also hard refresh the website using ctrl+F5 to bypass the cache.

Copyright Cal Origami 2021
