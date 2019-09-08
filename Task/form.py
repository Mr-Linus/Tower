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
        max_length=40,
        label="Image",
        help_text="镜像名称。"
    )
    path = forms.CharField(
        max_length=40,
        label="Path",
        help_text="代码存放的路径。"
    )
    cmd = forms.CharField(
        max_length=40,
        label="Command",
        help_text="执行的命令。"
    )



