from django import forms
from .models import jobd

class JdForm(forms.ModelForm):
    class Meta:
    	model= jobd
    	fields=['jd_id','company','field','designation','skills','education','experience']



class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'USERNAME',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'PASSWORD',
        max_length = 32,
        widget = forms.PasswordInput()
    )
   
class Loginform(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'USERNAME',
        max_length = 32
    )
    password = forms.CharField(
        required = True,
        label = 'PASSWORD',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    usertype = forms.CharField(
        required = True,
        label = 'User type (candidate/recruiter)',
        max_length = 32,
    )