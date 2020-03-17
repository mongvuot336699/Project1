
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login ,logout
from django.conf import settings
# from django.contrib import messages
# from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone

from .models import Item, OrderItem, Order, UserProfile , Category
from .form import UserProfileForm ,billForm
# Create your views here.

def category(request):
    cat = Category.objects.all()
    return render (request, "home/widget/category.html",{'cat':cat})

def productOfCat(request,pk):
    cat = Category.objects.get(pk=pk)
    return render (request,'home/widget/productOfCat.html', {'cat':cat } )

class HomeView(ListView):
    model = Item
    paginate_by = 3
    template_name = "home/widget/shop.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        object_list = Item.objects.all()
        paginator = Paginator(object_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['object_list'] = file_exams
        return context

class ItemDetailView(DetailView):
    model = Item
    template_name = "home/widget/shopSingle.html"


def add_to_cart(request, slug):
    if request.user.is_authenticated:
        item = get_object_or_404(Item, slug= slug)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            # check if the order item is in the order
            if order.items.filter(item__slug=item.slug).exists():
                order_item.quantity += 1
                order_item.save()
                return redirect("cart")
            else:

                order.items.add(order_item)
                return redirect("cart")
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(
                user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            return redirect("product", slug=slug)
    else:
        return redirect('login')

def remove_from_cart(request, slug):
    if request.user.is_authenticated:
        item = get_object_or_404(Item, slug=slug)
        order_qs = Order.objects.filter(
            user=request.user,
            ordered=False
        )
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(item__slug=item.slug).exists():
                order_item = OrderItem.objects.filter(
                    item=item,
                    user=request.user,
                    ordered=False
                )[0]
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                else:
                    order.items.remove(order_item)
                return redirect("cart")
            else:
                return redirect("product", slug=slug)
        else:
            return redirect("product", slug=slug)
    else:
        return redirect('login')

def cart(request):
    if request.user.is_authenticated:
        order = Order.objects.get(user=request.user, ordered=False)
        return render(request, "home/widget/cart.html", {
        'order':order,
        })
    else:
        return redirect('login')

def thankyou(request):
    return render (request, "home/widget/thankyou.html")

def registed(request):
    if request.method == 'POST':
        dangki = UserProfileForm(request.POST)
        if dangki.is_valid():
            dangki.save()
            return redirect('/thankyou')
    dangki = UserProfileForm()
    return render (request, 'home/widget/registed.html',{'dangki':dangki})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ("/")
        else:
            return redirect('login')
    return render(request, 'home/widget/login.html' )


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect ('thankyou')
    else:
        return redirect('/')

def checkout(request):
    if request.user.is_authenticated:
        order = Order.objects.get(user=request.user, ordered=False)
        if request.method == 'POST':
            form = billForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('thankyou')
            else:
                return redirect('checkout')
        bill = billForm()
        return render (request,'home/widget/checkout.html' ,{
            'bill':bill,
            'order':order,
        })
    else:
        return redirect('/')

# def removeCart(request,slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_qs = Order.objects.filter(
#         user=request.user,
#         ordered=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item = OrderItem.objects.filter(
#                 item=item,
#                 user=request.user,
#                 ordered=False
#             )[0]
#             order.items.remove(order_item)
#             return redirect ('cart')
#         else:
#             return redirect("product", slug=slug)
