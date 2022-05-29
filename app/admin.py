from django.contrib import admin

from .models import MainSlider


class MainSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'img_preview')
    readonly_fields = ('img_preview',)

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Img Preview'
    img_preview.allow_tags = True


admin.site.register(MainSlider, MainSliderAdmin)
