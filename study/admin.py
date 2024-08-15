from django.contrib import admin

from study.models import Study, Materials, Students


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'study_start')


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'study_materials', 'autor')


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('email', 'comment')

