from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from .forms import *
from datetime import date
from django.db.models import Count

# Create your views here.


def index(request):
    context = {
        "top_menus": Menu.objects.order_by("rating")[:5],
    }
    return render(request, "main/index.html", context=context)


@login_required
def my_profile(request):
    context = {
        "user": request.user
    }
    return render(request, "main/my_profile.html", context=context)


@login_required
def update_my_profile(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # if user.user_type == "staff":
            #     staff_form = StaffForm(request.POST)
            #     if staff_form.is_valid():
            #         staff = staff_form.save(commit=False)
            #         staff.user_id = user
            #         staff.save()
            return redirect('index')
        else:
            context["form"] = form
            # context["staff_form"] = staff_form
    else:
        context["form"] = RegisterForm(instance=request.user)
        # context["staff_form"] = StaffForm()
    return render(request, "main/update_my_profile.html", context=context)


@login_required
def my_orders(request):
    context = {
        "orders": Order.objects.filter(user_id=request.user).exclude(order_status="done")
    }
    return render(request, "main/my_orders.html", context=context)


@login_required
def my_history(request):
    context = {
        "orders": Order.objects.filter(user_id=request.user, order_status="done")
    }
    return render(request, "main/my_history.html", context=context)


def my_login(request):
    context = {
        "asd": "asd"
    }
    if request.method == "POST":
        form = LoginForm(request.POST)
        form.is_valid()
        user = authenticate(
            request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context["form"] = form
            context["alert"] = "Username or password is Wrong!"
    else:
        context["form"] = LoginForm()
    return render(request, "main/login.html", context=context)


@login_required
def my_logout(request):
    logout(request)
    return redirect("index")


def my_register(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # if user.user_type == "staff":
            #     staff_form = StaffForm(request.POST)
            #     if staff_form.is_valid():
            #         staff = staff_form.save(commit=False)
            #         staff.user_id = user
            #         staff.save()
            return redirect('index')
        else:
            context["form"] = form
            # context["staff_form"] = staff_form
    else:
        context["form"] = RegisterForm()
        # context["staff_form"] = StaffForm()
    return render(request, "main/register.html", context=context)


def report(request):
    context = {}
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user_id = request.user
            report.save()
            return redirect("index")
        else:
            context["form"] = form
    else:
        context["form"] = ReportForm()
    return render(request, "main/report.html", context=context)


def restaurants(request):
    user_id = request.user.id
    if not user_id:
        user_id = 0
    context = {
        "restaurants": Restaurant.objects.raw('''select *
        from main_restaurant r
        left outer join (select res_id_id, user_id_id
				from main_user_restaurant
                where user_id_id = %d) as u
        on (r.res_id = u.res_id_id)
        order by status desc, res_id''' % (user_id))
    }
    return render(request, "main/restaurants.html", context=context)


def restaurant(request, res_id):
    res = Restaurant.objects.get(pk=res_id)
    user_id = request.user.id
    if not user_id:
        user_id = 0
    context = {
        "restaurant": res,
        "voted": request.user in res.users.all(),
        "menus": Menu.objects.raw('''
        select *
        from main_menu m
        left outer join (select menu_id_id, user_id_id
				from main_user_menu
                where user_id_id = %d) as u
        on (m.menu_id = u.menu_id_id)
        where m.res_id_id = %d
        order by status desc, menu_id''' % (user_id, res.pk))
    }
    return render(request, "main/restaurant.html", context=context)


@login_required
def vote_restaurant(request, res_id, url):
    res = Restaurant.objects.get(pk=res_id)
    res.users.add(request.user)
    res.rating = res.users.count()
    res.save()
    return redirect(url)


@login_required
def unvote_restaurant(request, res_id, url):
    res = Restaurant.objects.get(pk=res_id)
    res.users.remove(request.user)
    res.rating = res.users.count()
    res.save()
    return redirect(url)


def menus(request):
    user_id = request.user.id
    if not user_id:
        user_id = 0
    context = {
        "menus": Menu.objects.raw('''select *
        from main_menu m
        left outer join (select menu_id_id, user_id_id
				from main_user_menu
                where user_id_id = %d) as u
        on (m.menu_id = u.menu_id_id)
        order by status desc, menu_id''' % (user_id))
    }
    return render(request, "main/menus.html", context=context)


def menu(request, menu_id):
    menu = Menu.objects.get(pk=menu_id)
    context = {
        "menu": menu,
        "voted": request.user in menu.users.all(),
        "extras": Extra.objects.filter(menu_id=menu_id)
    }
    return render(request, "main/menu.html", context=context)


@login_required
def vote_menu(request, menu_id, url):
    menu = Menu.objects.get(pk=menu_id)
    menu.users.add(request.user)
    menu.rating = menu.users.count()
    menu.save()
    return redirect(url)


@login_required
def unvote_menu(request, menu_id, url):
    menu = Menu.objects.get(pk=menu_id)
    menu.users.remove(request.user)
    menu.rating = menu.users.count()
    menu.save()
    return redirect(url)


@login_required
def my_restaurant(request):
    context = {}
    user = request.user
    if user.user_type == "staff":
        res = Staff.objects.get(pk=request.user).res_id
        if res:
            context["restaurant"] = res
        else:
            context["warning"] = "You do not work for Restauarant yet"
        return render(request, "main/my_restaurant.html", context=context)
    return redirect("index")


@login_required
def open_my_restaurant(request):
    user = request.user
    if user.user_type == "staff":
        res = Staff.objects.get(pk=request.user).res_id
        if res:
            res.status = "open"
            res.save()
    return redirect("my_restaurant")


@login_required
def close_my_restaurant(request):
    user = request.user
    if user.user_type == "staff":
        res = Staff.objects.get(pk=request.user).res_id
        if res:
            res.status = "close"
            res.save()
    return redirect("my_restaurant")


@login_required
def update_my_restaurant(request):
    context = {}
    user = request.user
    if user.user_type == "staff":
        res = Staff.objects.get(pk=request.user).res_id
        if res:
            if request.method == "POST":
                form = RestaurantForm(request.POST, instance=res)
                if form.is_valid():
                    form.save()
                    return redirect("my_restaurant")
                else:
                    context["form"] = form
            else:
                context["form"] = RestaurantForm(instance=res)
        else:
            context["warning"] = "You do not work for Restauarant yet"
        return render(request, "main/update_my_restaurant.html", context=context)
    return redirect("index")


def see_congestion(request):
    restaurants = Restaurant.objects.annotate(orders=Count('order'))
    context = {
        "restaurants": restaurants
    }
    return render(request, "main/see_congestion.html", context=context)


@login_required
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = request.user
            form.save()
            # messages.success(request, 'order has been sent!')
            return redirect('index')       
    else:
        form = OrderForm()
    return render(request, 'main/order.html', {'form': form})


@login_required
def sell_report(request):
    return None


@login_required
def my_restaurant_orders(request):
    return None


@login_required
def add_menu(request):
    return None
