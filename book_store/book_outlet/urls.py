from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index-page"),
    path('<int:id>/',views.book_detail,name="book-details-page"),
    path('<slug:slug>/',views.book_detail_slug,name="book-details-slug-page")
]