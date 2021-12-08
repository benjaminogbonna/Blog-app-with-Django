from django import forms
from .models import Comment

# a class for users to share posts to others
class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25, 
		widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Senders name'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
		'placeholder': 'Senders email'}))
	to = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
		'placeholder': 'Recipients email'}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))


# a class for users to comment on posts
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')
		widgets = {
            'name': forms.TextInput(
				attrs={
					'type':  'text',
					'class': 'form-control',
					'placeholder': 'Name'
					}
				),
            'email': forms.EmailInput(
				attrs={
					'type':  'email',
					'class': 'form-control',
					'placeholder': 'abc@domain.com'
					}
				),
             'body': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
			}


# A class for users to search for posts
class SearchForm(forms.Form):
	query = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 
			'placeholder': 'Type a keyword and hit enter',
			'type': 'text'}))


# A class for contact form
class ContactForm(forms.Form):
    name = forms.CharField(label='', 
    	widget=forms.TextInput(attrs={'class': 'form-control',
    		'placeholder': 'Your Name'}))

    email = forms.EmailField(label='', 
    	widget=forms.EmailInput(attrs={'class': 'form-control',
    		'placeholder': 'Your Email'}))

    subject = forms.CharField(label='', 
    	widget=forms.TextInput(attrs={'class': 'form-control',
    		'placeholder': 'Subject'}))

    message = forms.CharField(label='', 
    	widget=forms.Textarea(attrs={'class': 'form-control',
    		'placeholder': 'Message'}))
