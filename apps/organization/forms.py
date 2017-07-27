from django import forms

import re
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^[69]\d{9}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('Mobile invalid', code='mobile_invalid')

