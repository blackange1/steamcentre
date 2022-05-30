from django.shortcuts import render
from .models import Courses, ModuleOfCourses


def show_curses(request):
    courses = []
    for course in Courses.objects.all().order_by('number_of_courses'):
        modules = []
        modules_of_course = ModuleOfCourses.objects\
            .filter(courses=course)\
            .order_by('number_of_module')
        start = 1
        for module in modules_of_course:
            description = module.description.split('\n')
            modules.append(
                {
                    'name': module.name,
                    'number_of_module': module.number_of_module,
                    'img_module': module.img_module.url,
                    'description': description,
                    'start': start,
                }
            )
            start += len(description)
        courses.append(
            {
                'id': course.number_of_courses,
                'name': course.name,
                'age_of_student': course.age_of_student,
                'max_count_of_students': course.max_count_of_students,
                'background_color': course.background_color,
                'img_course': course.img_course.url,
                'description':  course.description.split('\n'),
                'modules': modules,
            }
        )
    return render(request, 'courses/courses.html', context={'courses': courses})
