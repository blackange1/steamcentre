from django.contrib import admin

from .models import Color, EduMaterial, EduСategory


class EduMaterialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color_preview',
        'like',
        'img_preview',
    )
    exclude = ('like',)
    list_filter = ('edu_сategory',)
    readonly_fields = ('img_preview',)

    search_fields = ('name', 'description')
    search_help_text = 'пошук здійснюється по назві та короткому опису'

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Img Preview'
    img_preview.allow_tags = True

    def color_preview(self, obj):
        return obj.color.color_preview


admin.site.register(EduMaterial, EduMaterialAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color_preview',
    )

    readonly_fields = ('color_preview',)

    def color_preview(self, obj):
        return obj.color_preview


admin.site.register(Color, ColorAdmin)


class EduСategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_long_name', 'type_category')

    def show_long_name(self, obj):
        if obj.long_name:
            return obj.long_name
        return obj.name


admin.site.register(EduСategory, EduСategoryAdmin)
