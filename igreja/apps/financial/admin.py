from django.contrib import admin

from .models import Installment, Payment


class InstallmentInline(admin.TabularInline):
    model = Installment


class PaymentAdmin(admin.ModelAdmin):
    inlines = [InstallmentInline]


admin.site.register(Payment, PaymentAdmin)
