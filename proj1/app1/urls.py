from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('products/',views.ProductView.as_view(),name="product"),
    path('products/',views.products,name='products'),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name='contact'),
    path('product_details/<int:id>',views.product_details,name='product_details'),
    path('whishlist/',views.whishlist,name='whishlist'),
    path('cart/',views.cart,name='cart'),
    path('orders/',views.orders,name='orders'),
    path('place_order_cart/',views.place_order_cart,name='place_order_cart'),
    path('place_order_buy/',views.place_order_buy,name='place_order_buy'),
    path('checkout/<slug:source>/',views.checkout,name='checkout'),
    path('error_page/',views.error_page,name='error_page'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('login/',views.cus_login,name='login'),
    path('logout/', views.lgout, name='logout'),
    path('add-to-cart/<int:prod_id>/', views.add_to_cart, name='add-to-cart'),
    path('add-to-cart-slug/<int:prod_id>/', views.add_to_cart_slug, name='add-to-cart-slug'),
    path('plus-cart/', views.plus_cart, name='plus-cart'),
    path('minus-cart/', views.minus_cart, name='minus-cart'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
