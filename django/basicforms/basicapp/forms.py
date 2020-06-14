from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with z")
class FormName(forms.Form):
    # name = forms.CharField(max_length=128,validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_cleaned_data = super().clean()
        email1 = all_cleaned_data['email']
        vmail = all_cleaned_data['verifyemail']
        if email1 != vmail:
            raise forms.ValidationError("EMAILS NOT SAME")
        # return self.all_cleaned_data
        
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('U SUCK BOT!')
    #     return botcatcher