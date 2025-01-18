"""
URL configuration for proj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),
    # path('',views.index,name='index'),
    # path('products/',views.products,name='products'),
    # path('contact/',views.contact,name='contact'),
    # path('product_details/',views.product_details,name='product_details'),
    # path('whishlist/',views.whishlist,name='whishlist'),
    # path('cart/',views.cart,name='cart'),
    # path('checkout/',views.checkout,name='checkout'),
    # path('error_page/',views.error_page,name='error_page'),
    # path('sign_up/',views.sign_up,name='sign_up'),
]
