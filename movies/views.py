from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Movie, Review
from .forms import ReviewForm, AddMovieForm, UpdateMovieForm


class MovieDetail(DetailView):
    """
    Displays individual movie from the Movie model
    and the related reviews to it.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Movie.objects.filter(approved=True)
        movie = get_object_or_404(queryset, slug=slug)
        reviews = movie.reviews.order_by('-created_on')

        return render(
            request,
            "movies/movie_detail.html",
            {
                "movie": movie,
                "reviews": reviews,
                "review_form": ReviewForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Movie.objects.filter(approved=True)
        movie = get_object_or_404(queryset, slug=slug)
        reviews = movie.reviews.order_by('-created_on')

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.author = request.user
            review = review_form.save(commit=False)
            review.movie = movie
            review.save()
            messages.success(request, 'Your Review has been added!')
        else:
            review_form = ReviewForm()

        return render(
            request,
            "movies/movie_detail.html",
            {
                "movie": movie,
                "reviews": reviews,
                "review_form": ReviewForm(),
            },
        )


class UpdateReview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Checks the user is logged in and allows them
    to update their review by fetching their current review
    and displaying it in a form. Redirects to home page
    when the form is submitted and displays a success message.
    """
    model = Review

    fields = [
        "rating",
        "review_content",
    ]

    template_name = 'movies/update_review.html'
    success_url = reverse_lazy('home')
    success_message = 'Updated Review successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_name'] = self.object.movie

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteReview(LoginRequiredMixin, DeleteView):
    """
    Checks the user is logged in and allows them to
    delete their review. Displays their current review
    and then deletes it when they submit the form. Redirects
    to home page on success and displays a message.
    """
    model = Review
    template_name = 'movies/delete_review.html'
    success_url = reverse_lazy('home')
    success_message = 'Review deleted succesfully!'

    # Success message on delete taken from:
    # https://stackoverflow.com/questions/48777015/djangos-successmessagemixin-not-working-with-deleteview
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message, 'danger')

        return super(DeleteReview, self).delete(request, *args, **kwargs)


class AddMovie(LoginRequiredMixin, CreateView):
    """
    Allows the user to request to add a movie using
    AddMovieForm. Redirects them to the home page when
    successful and displays a message.
    """
    model = Movie
    form_class = AddMovieForm
    template_name = 'movies/add_movie.html'

    def get_initial(self, *args, **kwargs):
        """
        Displays initial values in the Add movie form.
        """
        initial = super().get_initial(**kwargs)
        initial['name'] = 'Enter Movie Name'
        initial['director'] = 'Enter Movie Director'
        initial['summary'] = 'Enter a summary for the movie. NO SPOILERS!'
        return initial

    def post(self, request):
        if request.method == "POST":
            form = AddMovieForm(request.POST)
            if form.is_valid():
                new_movie = form.save(commit=False)
                new_movie.slug = slugify(new_movie.name)
                new_movie.save()
                messages.success(request, 'Add Movie request was successful!')
        form = AddMovieForm()
        return redirect("home")


class UpdateMovie(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    Checks the user is a superuser and then allows
    them to update an existing movie using the UpdateMovieForm.
    Redirects them to home page when successful and displays a
    message.
    """
    model = Movie
    form_class = UpdateMovieForm
    template_name = 'movies/update_movie.html'
    success_url = reverse_lazy('home')
    success_message = 'You have updated the Movie successfully!'

    def test_func(self):
        return self.request.user.is_superuser


class DeleteMovie(UserPassesTestMixin, DeleteView):
    """
    Checks the user is a superuser and then allows
    them to delete an existing movie from the Movie model.
    Redirects them to home page when successful and displays a
    message.
    """
    model = Movie
    template_name = 'movies/delete_movie.html'
    success_url = reverse_lazy('home')
    success_message = 'You have deleted the Movie successfully!'

    def test_func(self):
        return self.request.user.is_superuser

    # Success message on delete taken from:
    # https://stackoverflow.com/questions/48777015/djangos-successmessagemixin-not-working-with-deleteview
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message, 'danger')

        return super(DeleteMovie, self).delete(request, *args, **kwargs)
