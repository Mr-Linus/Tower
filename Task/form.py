from django import forms


class CreateNamespaceForm(forms.Form):
    namespace = forms.CharField(
        max_length=20,
        label="NameSpace",
        help_text="命名空间的名称，可以和用户名相同。",
        required=True
    )
