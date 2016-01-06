from django import forms

class UpdateTeam(forms.Form):
	team_name = forms.CharField(label='Team Name', max_length=200)