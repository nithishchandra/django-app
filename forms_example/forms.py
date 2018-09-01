from django import forms

from django.core.validators import ValidationError


#def validatename(value):
 #   if value.isdigit():
       # raise ValidationError('Digits are not allowed!')
#def validateemail(email):
 #   if email.split('@')[1] != 'mytectra.com':
  #      raise ValidationError('Email is Incorect')
class EmployeeForm(forms.Form):

    city_data = (
        ('', '--Make an option--'),
        ('Ananthapur', 'Ananthapur'),
        ('Kurnool', 'Kurnool'),
        ('Kadapa','Kadapa'),
        ('Nellore', 'Nellore'),
        ('Guntur', 'Guntur')
    )
    gn = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    im_not_robot = forms.CharField(widget=forms.CheckboxInput)
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    emp_name = forms.CharField(
        min_length=8,
        max_length=20,
        label='Employee Name',
        error_messages={
            'required': 'Enter a valid name ',
            'min_length': 'new error message'
        }
    )
    #im_not_robot = forms.CharField(widget=forms.CheckboxInput)
    #gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    emp_email = forms.EmailField()
    emp_addresss = forms.CharField(widget=forms.Textarea)
    emp_city = forms.ChoiceField(choices=city_data)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    pincode = forms.RegexField(regex='[0-9]{6}')
    file = forms.FileField()


    def clean(self):

        form_data = self.cleaned_data

        if 'emp_name' in form_data:
            if form_data['emp_name'].isdigit():
                self.errors['emp_name'] = ['Invalid name!']
        if 'emp_email' in form_data:
            if form_data['emp_email'].split('@')[1] != 'mytectra.com':
                self.errors['emp_email'] = ['Invalid Email!']

        if'password1' in form_data and 'password2' in form_data:
            if form_data['password1']!= form_data['password2']:
                self.errors['password1'] = ['password mismatch!']

        if 'pincode' in form_data:
            if len(form_data['pincode']) != 6:
                self.errors['pincode'] = ['Invalid Pincode']

        return form_data