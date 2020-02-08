from django.utils.translation import gettext_lazy as _
from User.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
import re


class CreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'name_lowcase': _("用户名必须小写英文字母开头,后面可加数字,不可设置符号."),
    }
    username = UsernameField(
        help_text="必填,用户名只含小写英文字母和数字组合,且必须小写英文字母开头,后面可加数字,不可设置符号."
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'QQ',
                  ]

    def CheckUsername(self):
        st = re.compile(r"^.*[0-9]")
        if len(re.findall(r'[A-Z]', self.cleaned_data.get('username'))) == 0:
            if "-" not in self.cleaned_data.get('username'):
                if "_" not in self.cleaned_data.get('username'):
                    if "@" not in self.cleaned_data.get('username'):
                        if not st.match(self.cleaned_data.get('username')):
                            return True
        self.add_error('username', error=self.error_messages['name_lowcase'])
        return False
