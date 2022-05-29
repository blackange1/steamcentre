from django.contrib import admin
from .models import Courses, ModuleOfCourses


class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age_of_student',
        'max_count_of_students',
        'img_preview',
    )
    readonly_fields = ('img_preview', )

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Img Preview'
    img_preview.allow_tags = True


admin.site.register(Courses, CoursesAdmin)


class ModuleOfCoursesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'courses',
        'number_of_module',
        'img_preview'
    )
    list_filter = (
        'courses',
    )

    readonly_fields = ('img_preview', )

    def img_preview(self, obj):
        return obj.img_preview

    img_preview.short_description = 'Img Preview'
    img_preview.allow_tags = True


admin.site.register(ModuleOfCourses, ModuleOfCoursesAdmin)
