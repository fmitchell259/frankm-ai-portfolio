from showcase_site import app, data_base
import os
from flask import (render_template, send_from_directory, abort, request,
                   flash, redirect, url_for)
from showcase_site.forms import ContactForm, PostForm
from showcase_site.models import PostProject
from flask_mail import Message, Mail

mail = Mail()


@app.route('/')
@app.route('/home')
def home():

    img_path = os.path.join(app.config['ANIM_FOLDER'], 'home_anim.mp4')

    return render_template('home.html',
                           home_img=img_path)


@app.route('/about')
def about():

    img_path = os.path.join(app.config['IMG_FOLDER'], 'about_face_2.jpg')
    mountain_img = os.path.join(app.config['IMG_FOLDER'], 'about_page.jpg')

    return render_template('about.html',
                           about_image = img_path,
                           mntn_img=mountain_img)


@app.route('/contact', methods=['GET', 'POST'])
def contact():

    form = ContactForm()

    if request.method == 'POST':
        if form.validate_on_submit():

            msg = Message(form.subject.data,
                          sender=app.config['MAIL_USERNAME'],
                          recipients=["frank.mitchell25@googlemail.com"])

            msg.body = '''
            From: %s <%s>
            %s
            ''' % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            flash("Message sent, I will get back to you shortly.", 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html',
                           form=form)


@app.route('/download_cv/<doc_name>')
def download_cv(doc_name):

    try:
        return send_from_directory(app.config["CV_FOLDER"],
                                   filename=doc_name,
                                   as_attachment=True)
    except FileNotFoundError:
        return abort(404)


@app.route('/projects')
def projects():

    posts = PostProject.query.all()

    python_img_path = os.path.join(app.config['IMG_FOLDER'], "python_logo_1.png")
    android_img_path = os.path.join(app.config['IMG_FOLDER'], "android_icon.png")
    html_img_path = os.path.join(app.config['IMG_FOLDER'], 'html_logo.png')

    return render_template('projects.html',
                           posts=posts,
                           python_img=python_img_path,
                           android_img=android_img_path,
                           html_img=html_img_path)


@app.route('/display_project/<post_id>')
def display_project(post_id):

    image_path = ''

    project = PostProject.query.get(post_id)

    if project.title == 'Genetic Algorithm':

        image_path = os.path.join(app.config['ANIM_FOLDER'], 'gen_vid.mp4')

    elif project.title == 'Tamagotchi on Android':

        image_path = os.path.join(app.config['IMG_FOLDER'], 'jake_image.jpg')

    elif project.title == 'Simulated Network':

        image_path = os.path.join(app.config['IMG_FOLDER'], 'network_image.jpg')

    elif project.title == 'Flask Site':

        image_path = os.path.join(app.config['IMG_FOLDER'], 'flask_site.png')

    return render_template('display_projects.html',
                           project=project,
                           img_path=image_path)

# Below we ave a route that will be made private, for now the user cannot openly link to it.

# Below we ave a route that will be made private, for now the user cannot openly link to it.


@app.route('/projects/new_post', methods=['GET', 'POST'])
def new_project():

    post_form = PostForm()

    if post_form.validate_on_submit():
        post = PostProject(lan=post_form.lan.data,
                            video=post_form.video.data,
                            title=post_form.title.data,
                            content=post_form.content.data)
        data_base.session.add(post)
        data_base.session.commit()
        flash("Project Post Created!.", 'success')
        return redirect(url_for('projects'))
    else:
        return render_template('create_post.html',
                                form=post_form)












