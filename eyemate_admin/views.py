from django.shortcuts import render

def no1(request):
    return render(request,'eyemate_admin/dashboard.html')

def no3(request):
    return render(request,'eyemate_admin/owner.html')

def no4fun(request):
    return render(request,'eyemate_admin/product_list_table.html')  

def no5fun(request):
    return render(request,'eyemate_admin/admin-login.html')    

def no7fun(request):
    return render(request,'eyemate_admin/admin-total-orders.html')

def no8fun(request):
    return render(request,'eyemate_admin/admin-manage-order.html')    

def no9fun(request):
    return render(request,'eyemate_admin/admin-total-product.html')        

def no10fun(request):
    return render(request,'eyemate_admin/admin-total-customer.html')         