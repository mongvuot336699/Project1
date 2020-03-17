from django.urls import path , include
from django.contrib import admin
from . import views
from .views import (
    HomeView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    cart,
    registed,
    user_login,
    user_logout,
    thankyou,
    category,
    productOfCat,
    checkout,
    # removeCart,
)

urlpatterns = [
    path('',category,name='category'),
    path('productOfCat/<int:pk>',productOfCat,name='productOfCat'),
    path('shop',HomeView.as_view(),name='shop'),
    path('shopSingle/<slug>/',ItemDetailView.as_view(),name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove_from_cart_url/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('cart',cart,name='cart'),
    # path('removeCart/<slug>',removeCart,name='removeCart'),
    path('checkout',checkout,name='checkout'),
    # cart and add card
    path('registed',registed,name='registed'),
    path('userlogin',user_login,name='login'),
    path('logout',user_logout,name='logout'),
    path('thankyou',thankyou,name='thankyou'),
    # user log in out
]
