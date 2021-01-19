from django import forms

class Contactenos(forms.Form):
	firstname=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Nombre'}), max_length=100)
	lastname=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Apellido'}), max_length=100)
	email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Correo'}), max_length=100)
	company=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Compañia'}), max_length=100)
	cargoem=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Cargo Empresa'}), max_length=100)
	phone=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}), max_length=100)
	city=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Ciudad'}), max_length=100)
	mensaje=forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Mensaje'}), max_length=500)
