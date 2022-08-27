from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductIndex(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'


class ProductView(DetailView):
    model = Product
    template_name = 'products/view.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/update.html'
    form_class = ProductForm
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "products/delete.html"
    permission_required = 'webapp.delete_product'

    def get_success_url(self):
        return reverse('webapp:product_index')