from django import forms
from django.forms.widgets import Select


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
        choices=(("tensorflow", "tensorflow"), ("pytorch", "pytorch")),
        initial="tensorflow",
        widget=Select()
    )
    version = forms.ChoiceField(
        label="Framework Version",
        help_text="使用的机器学习框架版本,例如:2.0。",
        choices=(("2.0", "2.0-(tensorflow)"), ("1.15", "1.15-(tensorflow)"), ("1.4", "1.4-(pytorch)")),
        initial="2.0",
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



