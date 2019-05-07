from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    TYPES = (
        ('user', 'user'),
        ('admin', 'admin'),
        ('staff', 'staff')
    )
    user_type = models.CharField(max_length=5, choices=TYPES, default='user')
    dob = models.DateField(null=True, blank=True)
    image_path = models.ImageField(
        default='user_images/default.png', upload_to='user_images', null=True, blank=True)

    def __str__(self):
        return self.username


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    create_time = models.DateTimeField(auto_now=True)
    TYPE = (
        ('canteen', 'canteen'),
        ('restaurant', 'restaurant'),
        ('other', 'other')
    )
    report_type = models.CharField(
        max_length=10, choices=TYPE, default='canteen')
    detail = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.user_id.username + " " + self.report_type


class Restaurant(models.Model):
    res_id = models.AutoField(primary_key=True)
    res_name = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    TYPE = (
        ('close', 'close'),
        ('open', 'open')
    )
    status = models.CharField(max_length=5, choices=TYPE, default='close')
    image_path = models.ImageField(
        default='restaurant_images/default.png', upload_to='restaurant_images', null=True, blank=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    Sunday = models.BooleanField(default=False, null=True, blank=True)
    Monday = models.BooleanField(default=False, null=True, blank=True)
    Tuesday = models.BooleanField(default=False, null=True, blank=True)
    Wednesday = models.BooleanField(default=False, null=True, blank=True)
    Thursday = models.BooleanField(default=False, null=True, blank=True)
    Friday = models.BooleanField(default=False, null=True, blank=True)
    Saturday = models.BooleanField(default=False, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=False, null=True, blank=True)
    users = models.ManyToManyField(
        User, through="User_restaurant", related_name="restaurants", blank=True)

    def __str__(self):
        return self.res_name


class User_restaurant(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class Staff(models.Model):
    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    res_id = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True, blank=True)


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    prepare_time = models.CharField(max_length=255, null=True, blank=True)
    image_path = models.ImageField(
        default='menu_images/default.png', upload_to='menu_images', null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    TYPE = (
        ('not_sell', 'not_sell'),
        ('sell', 'sell')
    )
    status = models.CharField(max_length=8, choices=TYPE, default='not_sell')
    rating = models.IntegerField(default=0, null=True, blank=True)
    users = models.ManyToManyField(
        User, through="User_menu", related_name="menus", blank=True)

    def __str__(self):
        return self.res_id.res_name + " " + self.menu_name


class User_menu(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class Extra(models.Model):
    class Meta:
        unique_together = (('extra_id', 'menu_id'),)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    extra_id = models.AutoField(primary_key=True)
    extra_name = models.CharField(max_length=255, null=True, blank=False)
    extra_description = models.TextField(null=True, blank=False)
    extra_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return '(%s) %s' % (self.menu_id.menu_name, self.extra_description)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    create_datetime = models.DateTimeField(auto_now=True)
    receive_datetime = models.DateTimeField(null=True, blank=False)
    comment = models.TextField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    TYPE = (
        ('ongoing', 'ongoing'),
        ('cancelled', 'cancelled'),
        ('ready', 'ready'),
        ('done', 'done'),
    )
    order_status = models.CharField(
        max_length=9, choices=TYPE, default='ongoing', null=True, blank=True)
    menus = models.ManyToManyField(
        Menu, through='Order_menu', related_name="orders", blank=True)

    def __str__(self):
        return '(%s) %s' % (self.user_id.username, self.create_datetime)


class Order_menu(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True, blank=False)
    TYPE = (
        ('preparing', 'preparing'),
        ('finished', 'finished')
    )
    status = models.CharField(
        max_length=9, choices=TYPE, default='preparing', null=True, blank=True)
