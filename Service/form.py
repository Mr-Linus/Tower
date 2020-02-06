from django import forms
from django.forms.widgets import Select


class CreateServiceForm(forms.Form):
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
