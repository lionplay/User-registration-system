from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Article

# Register your models here.

class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)