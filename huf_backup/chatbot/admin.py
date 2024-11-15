from django.contrib import admin
from .models import Question  # Import your models

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')

admin.site.register(Question, QuestionAdmin)  # Register your model
