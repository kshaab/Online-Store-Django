from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product, Contacts


def home(request):
    last_products = Product.objects.order_by("-created_at")[:5]
    for product in last_products:
        print(product)
    return render(request, "base.html")


def contacts(request):
    contact = Contacts.objects.first()
    return render(request, "contacts.html", {"contact": contact})


def contacts_post(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/templates/contacts.html")


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products_detail.html", context)


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)
    