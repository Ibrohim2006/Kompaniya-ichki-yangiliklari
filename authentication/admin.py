from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = ("email", "is_verified", "created_at")
    list_filter = ("first_name", "last_name", "es_verified")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions",
         {"fields": ("is_verified", "is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_verified", "is_staff", "is_active")}
         ),
    )

    search_fields = ("email",)
    ordering = ("-created_at",)
