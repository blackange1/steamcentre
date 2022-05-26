from django.contrib import admin

from .models import Courses, ModuleOfCourses


class CoursesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age_of_student',
        'max_count_of_students'
    )


admin.site.register(Courses, CoursesAdmin)


class ModuleOfCoursesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'courses',
        'number_of_module',
    )
    list_filter = (
        'courses',
    )


admin.site.register(ModuleOfCourses, ModuleOfCoursesAdmin)
