from django.contrib import admin
from .models import Post, Category, Metric, Tag
from .forms import PostForm
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ("title", "author", "content")
    list_filter = ("categories", )
    search_fields = ("title",)
    readonly_fields = ("author", )


class PostInline(admin.StackedInline):
    model = Post
    max_num = 3
    extra = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [PostInline]



admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Metric)
admin.site.register(Tag, TagAdmin)