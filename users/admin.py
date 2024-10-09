from django.contrib import admin

from users.models import Payment, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_of_payment', 'course_paid', 'lesson_paid', 'cost', 'payment_method')
    list_filter = ('user', 'date_of_payment', 'course_paid', 'lesson_paid', 'cost', 'payment_method')
    search_fields = ('payment_method',)