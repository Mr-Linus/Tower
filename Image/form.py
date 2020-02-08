from django import forms


class CreatePullForm(forms.Form):
    imageName = forms.CharField(
        max_length=20,
        label="镜像名称",
        help_text="容器镜像的名称，例如：helloworld:latest",
        required=True
    )

