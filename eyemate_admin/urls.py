from django.urls import path
from eyemate_admin import  views

urlpatterns = [
path('admin1', views.no1 ,name="admin1"),
path('owner', views.no3 ,name="owner"),
path('product_add_table', views.no4fun ,name="admin3"),
path('', views.no5fun ,name="admin-login"),


path('admin-total-orders', views.no7fun ,name="admin-total-orders"),
path('admin-manage-orders', views.no8fun ,name="admin-manage-orders"),
path('admin-total-products', views.no9fun ,name="admin-total-products"),
path('admin-total-customers', views.no10fun ,name="admin-total-customers"),

]