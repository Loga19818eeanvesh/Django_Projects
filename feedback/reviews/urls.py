from django.urls import path

from . import views

urlpatterns = [
    path("",views.ReviewView.as_view(),name="home"),
    path("thank-you",views.ThankyouView.as_view(),name="thank-you"),
    path("reviews",views.ReviewsListView.as_view(),name="reviews"),
    path("review/favorite/<int:id>",views.FavoriteView.as_view(),name="favorite-review"),
    path("reviews/<int:pk>",views.ReviewDetailView.as_view(),name="review-datail")
]