# accounts.admin.py

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

# Forms
# ----------------------------------------------------------------------------
class MyUserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class MyUserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin', 'phone', 'staff', 'active')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone')}),
        ('Personal info', {'fields': ('staff', 'active')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone', 'staff', 'active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)



# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)