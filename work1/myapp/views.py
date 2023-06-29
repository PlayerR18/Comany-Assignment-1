from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Order
from django.db.models import Sum


def home(request):
    return render(request, 'myapp/home.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        return redirect('myapp:user_dashboard')
    else:
        return render(request, 'myapp/user_signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('myapp:user_dashboard')
        else:
            error_message = "Invalid username or password"
            return render(request, 'myapp/user_login.html', {'error_message': error_message})
    else:
        return render(request, 'myapp/user_login.html')

def user_dashboard(request):
    return render(request, 'myapp/user_dashboard.html')

def admin_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email, is_staff=True, is_superuser=True)
        return redirect('myapp:admin_dashboard')
    else:
        return render(request, 'myapp/admin_signup.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff and user.is_superuser:
            login(request, user)
            return redirect('myapp:admin_dashboard')
        else:
            error_message = "Invalid username or password"
            return render(request, 'myapp/admin_login.html', {'error_message': error_message})
    else:
        return render(request, 'myapp/admin_login.html')

def admin_dashboard(request):
    return render(request, 'myapp/admin_dashboard.html')



def submit_order(request):
    if request.method == 'POST':
        user = request.POST['user']
        order_date = request.POST['order_date']
        company_name = request.POST['company_name']
        owner_name = request.POST['owner_name']
        item = request.POST['item']
        quantity = int(request.POST['quantity'])
        weight = float(request.POST['weight'])
        shipment_request = request.POST['shipment_request']
        tracking_id = request.POST['tracking_id']
        length = int(request.POST['length'])
        breadth = int(request.POST['breadth'])
        height = int(request.POST['height'])
        box_count = int(request.POST['box_count'])
        specification = request.POST['specification']
        quality_checklist = request.POST['quality_checklist']

        # Save the order details to the database or perform any other necessary operations

        success_message = "Order submitted successfully!"
        
        # Retrieve the user instance from the User model
        user_instance = User.objects.get(username=user)
        
        # Create the Order instance and assign the user instance
        order = Order(
            user=user_instance,
            order_date=order_date,
            company_name=company_name,
            owner_name=owner_name,
            item=item,
            quantity=quantity,
            weight=weight,
            shipment_request=shipment_request,
            tracking_id=tracking_id,
            length=length,
            breadth=breadth,
            height=height,
            box_count=box_count,
            specification=specification,
            quality_checklist=quality_checklist
        )
        order.save()

        return render(request, 'myapp/user_dashboard.html', {'success_message': success_message})
    else:
        return render(request, 'myapp/user_dashboard.html')




def admin_dashboard(request):
    orders = Order.objects.all()
    total_quantity = sum(order.quantity for order in orders)
    total_weight = sum(order.weight for order in orders)
    total_box = sum(order.box_count for order in orders)
    return render(request, 'myapp/admin_dashboard.html', {'orders': orders, 'total_quantity': total_quantity, 'total_weight': total_weight, 'total_box': total_box})



def logout_view(request):
    logout(request)
    return redirect('myapp:home')
