from django import forms


class CreateNamespaceForm(forms.Form):
    namespace = forms.CharField(
        max_length=20,
        label="NameSpace",
        help_text="命名空间的名称，可以和用户名相同。",
        required=True
    )


class CreateJobForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        label="Name",
        help_text="任务名称。"
    )
    namespace = forms.CharField(
        max_length=20,
        label="Namespace",
        help_text="输入你创建好的命名空间的名字。"
    )
    image = forms.CharField(
        max_length=80,
        label="Image",
        help_text="镜像名称。"
    )
    cmd = forms.CharField(
        max_length=140,
        label="Command",
        help_text="执行的命令。",
        required=False
    )



