from django import forms
from .models import User_detail

class UserdetailForm(forms.ModelForm):
	class Meta:
		model = User_detail
		fields = ['nick_name','email','age']