from django import forms


class ChangeCount(forms.Form):
    uid = forms.IntegerField(required=True)
    action = forms.CharField(max_length=1, required=True)


class DeleteItem(forms.Form):
    uid = forms.IntegerField(required=True)


class FinalizedAddress(forms.Form):
    id = forms.IntegerField()


class FinalizedCheckout(forms.Form):
    accept = forms.BooleanField(required=True, initial=False)


class AddItem(forms.Form):
    uid = forms.IntegerField(required=True)


class AddAddress(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    address = forms.CharField(
        max_length=500,
        required=True,
        widget=forms.Textarea(attrs={
            'rows': 10,
            'cols': 30,
            'placeholder': 'آدرس شما...',
        })
    )


class EditOrDeleteAddress(forms.Form):
    id = forms.IntegerField(required=False)
    # edit_flag = forms.BooleanField(required=False, initial=False)
    # delete_flag = forms.BooleanField(required=False, initial=False)
    # title = forms.CharField(max_length=50, required=True)
    # address = forms.CharField(
    #     max_length=500,
    #     required=True,
    #     widget=forms.Textarea(attrs={
    #         'rows': 10,
    #         'cols': 30,
    #         'placeholder': 'آدرس شما...',
    #     })
    # )