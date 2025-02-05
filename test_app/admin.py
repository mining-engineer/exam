#test_app/admin.py


from django.contrib import admin
from .models import Topic, TestQuestion, OpenQuestion, TestQuestionAnswer, OpenQuestionAnswer, TestResult

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('question',  'weight', 'topic')
    search_fields = ('question',)

@admin.register(OpenQuestion)
class OpenQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'weight', 'topic')
    search_fields = ('question',)

@admin.register(TestQuestionAnswer)
class TestQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_correct')
    search_fields = ('answer',)

@admin.register(OpenQuestionAnswer)
class OpenQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_answer')
    search_fields = ('correct_answer',)

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'question', 'student_answer', 'created_at')
    search_fields = ('student__username', 'question__text')