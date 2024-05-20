"""
URL configuration for shopeeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from shopeeapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("userlogout/", views.userlogout, name="userlogout"),
    path("mobilelist/", views.mobilelist, name="mobilelist"),
    path("shoeslist/", views.shoeslist, name="shoeslist"),
    path("clothlist/", views.clothlist, name="clothlist"),
    path("electronicslist/", views.electronicslist, name="electronicslist"),
    path("pricerangeview/", views.pricerangeview, name="pricerangeview"),
    path("allsortedproducts", views.allsortedproducts, name="allsortedproducts"),
    path("searchproduct/", views.searchproduct, name="searchproduct"),
    path("showcarts/", views.showcarts, name="showcarts"),
    path("addtocart/<int:productid>", views.addtocart, name="addtocart"),
    path("removecart/<int:productid>", views.removecart, name="removecart"),
    path("updateqty/<int:qv>/<int:productid>", views.updateqty, name="updateqty"),
    path("payment/", views.payment, name="payment"),
    path("showorders", views.showorders, name="showorders"),
    path("registerproduct", views.registerproduct, name="registerproduct"),
    path("showregisterproduct", views.showregisterproduct, name="showregisterproduct"),
    path(
        "removeregisterproduct/<int:productid>",
        views.removeregisterproduct,
        name="removeregisterproduct",
    ),
    path(
        "updateregisterproduct/<int:productid>",
        views.updateregisterproduct,
        name="updateregisterproduct",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
