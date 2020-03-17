from django import forms
from .models import UserProfile , bill
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'cus_username'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'cus_first_name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'cus_last_name'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'cus_email'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'password',
    'class':'form-control',
    'id':'cus_password1'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'password',
    'class':'form-control',
    'id':'cus_password2'
    }))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class billForm(forms.ModelForm):
    country = forms.CharField(widget=forms.TextInput(attrs={
    # 'type': 'text-black',
    'class':'form-control',
    'id':'c_country'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'c_fname'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'c_lname'
    }))
    company_name = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'c_companyname'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'c_address'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'c_email_address'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'c_phone'
    }))
    order_note = forms.CharField(widget=forms.Textarea(attrs={
    'type': 'text',
    'class':'form-control',
    'id':'c_order_notes',
    'cols':'30',
    'rows':'5',
    }))

    class Meta:
        model = bill
        fields = '__all__'
