from django.contrib import admin
from users.models import CustomUser, Group


# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'status', 'group')
    fields = (
        ('first_name', 'last_name', 'email', 'username'),
        ('group', 'status'),
        ('is_superuser', 'is_staff'),
        'date_joined',
        'user_permissions',
        'groups',
    )

    list_filter = ('is_superuser', 'is_staff', 'is_active')
    search_fields = ('last_name',)
    readonly_fields = ('date_joined', 'username', 'password', 'first_name', 'last_name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', )
