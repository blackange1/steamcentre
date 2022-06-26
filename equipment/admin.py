from django.contrib import admin

from .models import Laboratory, Product


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'number_of_lab',
        'img_preview',
    )
    readonly_fields = ('img_preview',)

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Img Preview'
    img_preview.allow_tags = True


admin.site.register(Laboratory, LaboratoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'lab',
        'number_of_products',
        'img_preview',
    )
    list_filter = (
        'lab',
    )

    search_fields = ('name',)
    search_help_text = 'пошук здійснюється по назві'

    readonly_fields = ('img_preview',)

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Img Preview'
    img_preview.allow_tags = True


admin.site.register(Product, ProductAdmin)
