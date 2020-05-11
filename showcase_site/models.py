from showcase_site import data_base
from datetime import datetime


class PostProject(data_base.Model):

    id = data_base.Column(data_base.Integer, primary_key=True)
    lan = data_base.Column(data_base.String(100), nullable=False)
    video = data_base.Column(data_base.String(10), nullable=False)
    title = data_base.Column(data_base.String(100), nullable=False)
    date_posted = data_base.Column(data_base.DateTime, nullable=False, default=datetime.utcnow)
    content = data_base.Column(data_base.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"