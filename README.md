# calorigami.berkeley.edu

## Update:
The website is currently being updated to use the Flask templating system more
extensively to make it easier to edit by future webmasters. New information
should be placed in `/data/` and it should be parsed and updated accordingly
on the website.

### Pages currently using new templates:
* `templates/officers.html`
* `templates/index.html` (in progress)

## Background:
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
