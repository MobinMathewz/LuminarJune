from django.urls import path
from myapp.views import createAuthor,createBook,bookView,bookEdit,listBook,bookDelete

urlpatterns = [
    path('authcreate/',createAuthor,name="authorcreate"),
    path('bookcreate/',createBook,name="bookcreate"),
    path('bookview/<int:pk>',bookView,name="viewBook"),
    path('bookedit/<int:pk>',bookEdit,name="editBook"),
    path('bookdelete/<int:pk>',bookDelete,name="deleteBook"),
    path('listbook/',listBook,name="listBook"),
]