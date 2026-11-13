from django.contrib import admin
# Import seven models
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission


# QuestionInline for CourseAdmin
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


# ChoiceInline for QuestionAdmin
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5


# LessonInline for CourseAdmin
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# QuestionAdmin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']


# LessonAdmin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# CourseAdmin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
