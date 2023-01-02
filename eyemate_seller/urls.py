from django.urls import path
from eyemate_seller import  views

urlpatterns = [
path('', views.sellerloginfun ,name="seller_login"),
path('seller_register', views.sellerregisterfun ,name="seller_register"),
path('seller-dashboard', views.sellerhomefun ,name="seller-dashboard"),
path('seller_master', views.masterfun ,name="seller_master"),
path('add_product', views.addproductfun ,name="add_product"),
path('manage_orders', views.sellermanageordersfun ,name="manage_orders"),
path('seller-total-product', views.sellertotalproductfun ,name="seller-total-product"),
path('seller-total-customers', views.sellertotalcustomerfun,name="seller-total-customers"),
]