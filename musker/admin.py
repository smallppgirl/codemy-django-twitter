from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep

# Unregister Groups
admin.site.unregister(Group)


# Mix Profile info into user Info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


# Unregister initial User
admin.site.unregister(User)

# Register User
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

# Register Meeps
admin.site.register(Meep)

