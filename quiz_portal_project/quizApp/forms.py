from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'user_type', 'password1','password2']

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'
        
class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username','password']

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user'] 

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'
        
class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = '__all__'
        

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionModel
        fields = '__all__'
        exclude = ['quiz']
        

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'
        
class OptionForm(forms.ModelForm):
    class Meta:
        model = OptionModel
        fields = '__all__'
        exclude = ['question']

        

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class']='form-control'
        