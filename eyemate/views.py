from urllib import request
from django.shortcuts import render

def test(request):
    return render(request,'eyemate/home.html')

def test1(request):
    return render(request,'eyemate/about.html') 

def test3(request):
    return render(request,'eyemate/contact.html')

def test4(request):
    return render(request,'eyemate/products.html')

def test5(request):
    return render(request,'eyemate/cart.html')

def test6(request):
    return render(request,'eyemate/login.html')

def test7(request):
    return render(request,'eyemate/register.html')

def test8(request):
    return render(request,'eyemate/blogs.html')   

def master(req):
    return render(req, 'eyemate/master.html') 

def test9(request):
    return render(request, 'eyemate/checkout.html') 

def test10(request):
    return render(request,'eyemate/premium.html')   

def test11(request):
    return render(request, 'eyemate/computer.html') 

def test12(request):
    return render(request, 'eyemate/sun.html') 

def test13(request):
    return render(request, 'eyemate/products_details.html') 

def test14(request):
    return render(request, 'eyemate/wishlist.html') 

def test15(request):
    return render(request,'eyemate/user-profile.html')

# def test15(request):
#     return render(request, 'eyemate/user-profile.html') 
