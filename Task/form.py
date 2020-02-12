from django import forms
from django.forms.widgets import Select
import re
from django.utils.translation import gettext_lazy as _


class CreateNamespaceForm(forms.Form):

    namespace = forms.ChoiceField(
        label="NameSpace",
        help_text="一键创建命名空间,与用户名相同。",
        required=True,
        choices=((0, "用户名称"),),
        initial=0,
        widget=Select()
    )


class CreateJobForm(forms.Form):
    error_messages = {
        'name_lowcase': _("任务名称,任务名必须小写英文字母开头,后面可加数字,不可设置符号。"),
    }
    name = forms.CharField(
        max_length=20,
        label="Name",
        help_text="任务名称。",
        required=True
    )
    gpu = forms.ChoiceField(
        label="GPU",
        help_text="使用的GPU数量。",
        choices=(("0", "0 - (使用CPU)"), ("1", "1")),
        initial="1",
        widget=Select()
    )
    memory = forms.ChoiceField(
        label="GPU Memory",
        help_text="使用的显存大小,单位: MB。若使用CPU,此项无效。",
        choices=(("0", "0 - (使用CPU)"), ("1000", "1000MB"), ("2000", "2000MB"),
                 ("4000", "4000MB"), ("8000", "8000MB"), ("10000", "10000MB")),
        initial="1000",
        widget=Select()
    )
    level = forms.ChoiceField(
        label="GPU 等级",
        help_text="使用的GPU性能,若使用CPU,此项无效。",
        choices=(("Low", "Low - GeForce GT 720"),
                 ("Medium", "Medium - GeForce GTX 1660"), ("High", "High - GeForce GTX Titan Xp")),
        initial="Medium",
        widget=Select()
    )
    framework = forms.ChoiceField(
        label="Framework",
        help_text="使用的深度学习框架类型。",
        choices=(("tensorflow-2.0", "tensorflow-v2.0"), ("tensorflow-1.15", "tensorflow-v1.15"),
                 ("pytorch-1.4", "pytorch-v1.4")),
        initial="tensorflow-2.0",
        widget=Select()
    )

    type = forms.ChoiceField(
        label="Type",
        help_text="任务工作类型。",
        choices=(("ssh", "ssh"), ("train", "train")),
        initial="ssh",
        widget=Select()
    )
    cmd = forms.CharField(
        max_length=140,
        label="Command",
        help_text="执行的命令。若工作类型为'ssh',此项无效。",
        required=False
    )

    def is_valid(self):
        st = re.compile(r"^[0-9]")
        if len(re.findall(r'[A-Z]', self.data.get('name'))) == 0:
            if "-" not in self.data.get('name'):
                if "_" not in self.data.get('name'):
                    if "@" not in self.data.get('name'):
                        if not st.match(self.data.get('name')):
                            return self.is_bound and not self.errors
        self.add_error('name', error=self.error_messages['name_lowcase'])
        return self.is_bound and not self.errors



