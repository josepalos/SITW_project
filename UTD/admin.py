from django.contrib import admin
import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(models.Album)
admin.site.register(models.Artist)
admin.site.register(models.Song)
admin.site.register(models.Provider)
admin.site.register(models.UserArtistsList)
admin.site.register(models.Playlist)


# Use UserProfile as user model.
# FROM (https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#extending-the-existing-user-model)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = models.UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)