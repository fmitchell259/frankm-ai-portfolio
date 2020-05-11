from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):

    name = StringField("Your Name",
                       validators=[DataRequired()])
    email = StringField("Your Email",
                        validators=[DataRequired(),
                                    Email()])
    subject = StringField("Subject",
                          validators=[DataRequired()])
    message = TextAreaField("Message",
                            validators=[DataRequired()])
    submit = SubmitField("Send")


class PostForm(FlaskForm):

    lan = StringField('Language?',
                      validators=[DataRequired()])
    video = StringField('Video?',
                        validators=[DataRequired()])
    title = StringField('Title',
                        validators=[DataRequired()])
    content = TextAreaField('Content',
                            validators=[DataRequired()])
    submit = SubmitField('Post')

