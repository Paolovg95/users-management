from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Empresa, UserProfile

admin.site.register(Empresa)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # Columns
    list_display = ("email","group_name", "is_staff", "is_active")
    # Filters
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active","is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    def group_name(self,obj):
        return f"{obj.groups.first()}"
    group_name.short_description = "Group"

    search_fields = ("email",)
    ordering = ("email",)
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    model = UserProfile
    list_display = ("full_name","group_name","mi_empresa",)


    def mi_empresa(self, obj):
        return obj.empresa
    mi_empresa.short_description = "Empresa"
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = "Full Name"
    def group_name(self, obj):
        return f"{obj.user.groups.first()}"
    group_name.short_description = "Group"
