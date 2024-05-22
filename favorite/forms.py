from django import forms


class BookMarkForm(forms.Form):
    uid = forms.IntegerField(required=True)
