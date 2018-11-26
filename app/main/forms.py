from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.' ,validators = [Required()])

    submit = SubmitField('Submit')
class BlogForm(FlaskForm):
    title = StringField('title',validators=[Required()])
    blog = TextAreaField('Write your blog here',validators=[Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
    description = TextAreaField('Add comment',validators = [Required()])
    Submit = SubmitField('submit')
