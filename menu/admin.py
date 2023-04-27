from django.contrib import admin
from menu.models import MainMenu, AnotherMenu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_display_links = ('name', 'parent')
    search_fields = ('name', 'parent')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


admin.site.register(MainMenu, MenuAdmin)
admin.site.register(AnotherMenu, MenuAdmin)
