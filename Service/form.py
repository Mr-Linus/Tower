from django import forms
from django.forms.widgets import Select
import re
from django.utils.translation import gettext_lazy as _


class CreateServiceForm(forms.Form):
    error_messages = {
        'name_lowcase': _("任务名称,任务名必须小写英文字母开头,后面可加数字,不可设置符号。"),
    }
    name = forms.CharField(
        max_length=20,
        label="Name",
        help_text="关联的任务名称。",
        required=True
    )
    port = forms.ChoiceField(
        label="Port",
        help_text="用于SSH的通信端口",
        required=True,
        choices=((0, "自动生成"),),
        initial=0,
        widget=Select()
    )

    def is_valid(self):
        s = re.compile(r"^[0-9]")
        if len(re.findall(r'[A-Z]', self.data.get('name'))) == 0:
            if "-" not in self.data.get('name'):
                if "_" not in self.data.get('name'):
                    if "@" not in self.data.get('name'):
                        if not s.match(self.data.get('name')):
                            return self.is_bound and not self.errors
        self.add_error('name', error=self.error_messages['name_lowcase'])
        return self.is_bound and not self.errors
