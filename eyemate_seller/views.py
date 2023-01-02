from django.shortcuts import render


def masterfun(request):
    return render(request,'eyemate_seller/seller_master.html')

def sellerhomefun(request):
    return render(request,'eyemate_seller/seller-home.html')

def addproductfun(request):
    return render(request,'eyemate_seller/seller-add-product.html')

def sellerloginfun(request):
    return render(request,'eyemate_seller/seller_login.html')

def sellerregisterfun(request):
    return render(request,'eyemate_seller/seller_register.html')

def sellermanageordersfun(request):
    return render(request,'eyemate_seller/seller-manage-order.html')

def sellertotalcustomerfun(request):
    return render(request,'eyemate_seller/seller-total-customers.html')

def sellertotalproductfun(request):
    return render(request,'eyemate_seller/seller-total-product.html')

