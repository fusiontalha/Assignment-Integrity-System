from django.contrib import admin
from .models import Course, Assignment, AssignmentSubmission,AssignmentResult

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(AssignmentResult)
# @admin.register(AssignmentResult)
# class AssignmentResultAdmin(admin.ModelAdmin):
#     List_display = ['id','user','marks','comments']
