
from pyexpat import model
from re import template
from traceback import format_exc
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

'''class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request,'reviews/review.html',{
            "form":form
        })
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid() :
            """
            review = Review(
                user_name = form.cleaned_data['user_name'],
                review_text = form.cleaned_data['review_text'],
                rating = form.cleaned_data['rating']
            )
            review.save()
            """
            form.save()
            return redirect('thank-you')

        return render(request,'reviews/review.html',{
            "form":form
        })
'''

'''class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = "/thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        '''

class FavoriteView(View):
    def post(self,request,*args, **kwargs):
        review_id = kwargs['id']
        #favorite_review = Review.objects.get(pk=review_id)
        #print(request.session)
        request.session["favorite_review"] = review_id
        return redirect('review-datail',pk=review_id)


class ReviewView(CreateView):
    model = Review
    #fields = '__all__'
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = "/thank-you"

class ThankyouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "This works!"
        return context

class ReviewsListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = "reviews"
    """
    def get_queryset(self):
        base_query =  super().get_queryset()
        data = base_query.filter(rating__gte=2)
        return data
    """

class ReviewDetailView(DetailView):
    template_name = 'reviews/review_detail.html'
    model = Review

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        #print(favorite_id)
        #print(loaded_review.id)
        context["is_favorite"] = str(favorite_id) == str(loaded_review.id)
        #print(context["is_favorite"])
        return context


'''class ReviewDetailView(TemplateView):
    template_name = 'reviews/review_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        review = Review.objects.get(id=review_id)
        context['review'] = review
        return context
        '''


def review(request):

    if(request.method == "POST"):
        form = ReviewForm(request.POST)
        if form.is_valid() :
            """
            review = Review(
                user_name = form.cleaned_data['user_name'],
                review_text = form.cleaned_data['review_text'],
                rating = form.cleaned_data['rating']
            )
            review.save()
            """
            form.save()
            return redirect('thank-you')
    else:
        form = ReviewForm()
        
    return render(request,'reviews/review.html',{
        "form":form
    })

def thank_you(request):
    return render(request,'reviews/thank_you.html')


