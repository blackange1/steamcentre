from django.contrib import admin

from .models import Profile, Comment, SubComment


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'img_preview',
    )

    readonly_fields = ('user', 'img_preview', 'collection_material', 'liked')

    def img_preview(self, obj):
        return obj.img_preview


admin.site.register(Profile, ProfileAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text_comment',
        'user',
        'edu_material',
        'date'
    )

    search_fields = ('text',)
    search_help_text = 'пошук здійснюється по вмісту коментаря'

    def text_comment(self, obj):
        if len(obj.text) >= 50:
            return obj.text[:50] + '...'
        return obj.text


admin.site.register(Comment, CommentAdmin)


class SubCommentAdmin(admin.ModelAdmin):
    list_display = (
        'text_comment',
        'user',
        'date'
    )

    search_fields = ('text',)
    search_help_text = 'пошук здійснюється по вмісту коментаря'

    def text_comment(self, obj):
        if len(obj.text) >= 50:
            return obj.text[:50] + '...'
        return obj.text


admin.site.register(SubComment, SubCommentAdmin)
