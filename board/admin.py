from django.contrib import admin

# Register your models here.

from .models import Question, Category

#admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('name')
    search_fields = ['name']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)