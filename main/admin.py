from django.contrib import admin
from main.models import User, Report, Restaurant, Menu, Extra, Order, Staff
from django.contrib.auth.models import Permission

admin.site.register(Permission)


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_type', 'dob']
    list_per_page = 15
    list_filter = ['user_type', 'dob']
    search_fields = ['username']

    fieldsets = [
        (None, {'fields': ['username', 'user_type', 'first_name',
                           'last_name', 'email', 'dob', 'image_path']}),
        ("User Permissions", {
            'fields': ['groups', 'user_permissions'], 'classes': ['collapse']})
    ]


admin.site.register(User, UserAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ['user_id', "res_id"]
    list_per_page = 15
    list_filter = ["res_id"]


admin.site.register(Staff, StaffAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'report_type', 'create_time', 'detail']
    list_per_page = 15
    list_filter = ['report_type', 'create_time']
    search_fields = ['detail']


admin.site.register(Report, ReportAdmin)


class MenuInline(admin.StackedInline):
    model = Menu
    extra = 3


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['res_id', 'res_name', 'status', 'owner']
    list_per_page = 15
    list_filter = ['status', 'rating', 'open_time', 'close_time']
    search_fields = ['res_name']

    fieldsets = [
        (None, {'fields': ['res_name', 'description',
                           'owner', 'status', 'image_path']}),
        ("Time Management", {'fields': ['open_time', 'close_time', 'Sunday', 'Monday',
                                        'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 'classes':['collapse']}),
    ]

    inlines = [MenuInline]


admin.site.register(Restaurant, RestaurantAdmin)


class ExtraInline(admin.StackedInline):
    model = Extra
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    list_display = ['menu_id', 'menu_name',
                    'res_id', 'price', 'status', 'rating']
    list_per_page = 15
    list_filter = ['price', 'status', 'rating', 'prepare_time']
    search_fields = ['menu_name']

    inlines = [ExtraInline]


admin.site.register(Menu, MenuAdmin)


class ExtraAdmin(admin.ModelAdmin):
    list_display = ['menu_id', 'extra_name',
                    'extra_description', 'extra_price']
    list_per_page = 15
    list_filter = ['extra_price']
    search_fields = ['menu_name']


admin.site.register(Extra, ExtraAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'create_datetime',
                    'receive_datetime', 'total_price', 'user_id']
    list_per_page = 15
    list_filter = ['create_datetime', 'total_price', 'user_id']
    search_fields = ['menu_name']


admin.site.register(Order, OrderAdmin)
