from django.forms import ModelForm
from myapp.models import Author, MyBook

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["author_name"]

        def clean(self):
            print("inside clean")


class BookForm(ModelForm):
    class Meta:
        model = MyBook
        fields = "__all__"


class BookEditForm(ModelForm):
    class Meta:
        model = MyBook
        fields = "__all__"