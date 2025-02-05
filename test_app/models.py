#test_app/models.py

from django.db import models
from user_app.models import User 

class Topic(models.Model):
    """таблица с темами вопросв"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class TestQuestion(models.Model):
    """таблица с вопрсоами для тестирования"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='test_questions')
    question = models.TextField()
    weight = models.IntegerField(default=1)  # Вес вопроса в баллах
    count_variant = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.text}"
    

class OpenQuestion(models.Model):
    """таблица с открытыми вопросами"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='open_questions')
    question = models.TextField()
    weight = models.IntegerField(default=1)  # Вес вопроса в баллах

    def __str__(self):
        return f"{self.text}"


class TestQuestionAnswer(models.Model):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='test_answers')
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} (Правильный: {self.is_correct})"


class OpenQuestionAnswer(models.Model):
    question = models.OneToOneField(OpenQuestion, on_delete=models.CASCADE, related_name='open_answer')
    correct_answer = models.TextField()

    def __str__(self):
        return f"Правильный ответ: {self.correct_answer}"


class TestResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results')
    topic = models.TextField()
    question = models.TextField()
    student_answer = models.TextField(blank=True, null=True)  # Ответ студента
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.question.text} - {self.student_answer.text}"