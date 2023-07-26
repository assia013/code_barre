from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Marque, Produit,code_serie

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
#admin.site.register(User, UserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['nom']
admin.site.register(Category,CategoryAdmin)

class marqueAdmin(admin.ModelAdmin):
    search_fields = ['nom']
admin.site.register(Marque,marqueAdmin)

class produitAdmin(admin.ModelAdmin):
    list_display = ('num','nom','categorie', 'marque')
    search_fields = ['nom']
admin.site.register(Produit,produitAdmin)

class code_serieAdmin(admin.ModelAdmin):
    list_display = ('code','produit')
    search_fields = ['code']
admin.site.register(code_serie,code_serieAdmin)