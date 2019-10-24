from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class PitchForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    category = SelectField('Category',choices=[('Interview','Interview'),('Events','Events'),('Job','Job')],validators=[Required()])
    post = TextAreaField('Your idea',validators=[Required()])
    submit = SubmitField('Share your idea')