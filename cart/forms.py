from django import forms


class ChangeCount(forms.Form):
    uid = forms.IntegerField(required=True)
    action = forms.CharField(max_length=1, required=True)


class DeleteItem(forms.Form):
    uid = forms.IntegerField(required=True)
