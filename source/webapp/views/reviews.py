from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from webapp.forms import ReviewForm, ReviewModerForm
from webapp.models import Review, Product


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/create.html'
    permission_required = 'webapp.add_task'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect('webapp:product_view', pk=product.pk)


class ReviewUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'reviews/update.html'
    form_class = ReviewForm
    permission_required = 'webapp.change_review'

    def has_permission(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == review.author

    def form_valid(self, form):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        form = form.save(commit=False)
        form.status = False
        form.save()
        return redirect('webapp:product_view', pk=review.product.pk)


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = "reviews/delete.html"
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == review.author

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.product.id})


class ReviewView(PermissionRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/index.html'
    context_object_name = 'reviews'
    permission_required = 'webapp.can_view_false_reviews'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        reviews = Review.objects.filter(status=False).order_by('-updated_at')
        context['reviews'] = reviews
        return context


class ReviewModerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Review
    template_name = 'reviews/moder_update.html'
    form_class = ReviewModerForm
    permission_required = 'webapp.change_review'

    def has_permission(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('pk'))
        return super().has_permission() or self.request.user == review.author

    def get_success_url(self):
        return reverse('webapp:review_index')