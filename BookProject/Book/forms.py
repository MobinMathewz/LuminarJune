from django import forms

#bname,authorname,noofpages,price,category

class BookForm(forms.Form):
    bookname = forms.CharField(max_length=150)
    author = forms.CharField(max_length=120)
    pages = forms.IntegerField()
    price = forms.IntegerField()
    category = forms.CharField(max_length=120)

    def clean(self):
        cleaned_data = super().clean()
        pages = cleaned_data.get("pages")
        print(pages)
        if (pages<10):
            message = "Enter valid page number"
            self.add_error('pages', message)

        price = cleaned_data.get("price")
        print(price)
        if (price<50):
            message = "Enter a valid price"
            self.add_error('price',message)