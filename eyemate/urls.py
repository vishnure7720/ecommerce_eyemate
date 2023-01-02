from django.urls import path
from.import  views

urlpatterns = [
    path('master',views.master, name='master'),
    path('', views.test ,name="store"),
    path('about', views.test1 ,name="store2"),
    path('contact', views.test3 ,name="store3"),
    path('products', views.test4 ,name="store4"),
    path('cart', views.test5 ,name="store5"),
    path('login', views.test6 ,name="store6"),
    path('register', views.test7 ,name="store7"),
    path('blogs', views.test8 ,name="store8"),
    path('checkout', views.test9 ,name="store9"),
    path('premium', views.test10 ,name="store10"),
    path('computer', views.test11 ,name="store11"),
    path('sun', views.test12 ,name="store12"),
    path('products_details', views.test13 ,name="store13"),
    path('wishlist', views.test14 ,name="store14"), 
    path('user-profile',views.test15, name="store15"),
    # path('user-profile', views.test15 ,name="store15"),


]


