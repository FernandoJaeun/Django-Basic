from django.contrib import admin

from .models import Question,Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text']  # 표시항목 순서 변경
    fieldsets = [
        (None, {'fields': ['question_text']}),
        #('Date Information', {'fields' : ['pub_date']})
        ('Date Information', {'fields' : ['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')    # 레코드 리스트 항목 지정 황목의 카테고리 표시
    list_filter = ['pub_date']  # 리스트를 날짜로 찾을 수 있게 필터창을 제공
    search_fields = ['question_text']   # 퀘테를 검색해서 찾을 수 있게 검색바 제공
# 이 클래스를 admin.site.register에 추가하면 웹에서 필드가 분리됨




admin.site.register(Question,QuestionAdmin)   
admin.site.register(Choice)