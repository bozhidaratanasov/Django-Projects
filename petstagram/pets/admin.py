from pets.models import Comment, Like, Pet
from django.contrib import admin

class LikeInlineAdmin(admin.TabularInline):
    model = Like

class PetAdmin(admin.ModelAdmin):
    # fields = ('type', 'name')
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')
    inlines = [
        LikeInlineAdmin
    ]


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
admin.site.register(Comment)