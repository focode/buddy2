from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.usersProfiles
        fields = "__all__"



class boozProfilesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(boozProfilesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.boozProfiles
        fields = "__all__"


class LocateDrinkersForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LocateDrinkersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.locateDrinkers
        fields = "__all__"




