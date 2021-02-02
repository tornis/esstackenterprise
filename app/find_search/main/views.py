from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib import messages
from .models import Product

class HomePageView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.info(self.request, "hello http://example.com")
        return context


def searchTerm(request):
    context = {}
    template_name = "main/index.html"
    if request.method == "POST":
        termo = request.POST["busca_termo"]
        produto = Product.objects.filter(product_name__contains=termo)
        context['PRODUTOS'] = produto
        return render(request, template_name,context)
    else:
        return render(request, template_name, context)
