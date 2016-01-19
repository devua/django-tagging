"""
Admin components for tagging.
"""
from django.contrib import admin

from tagging.models import Tag
from tagging.models import TaggedItem
from tagging.forms import TagAdminForm


class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm

    class Meta:
        fields = '__all__'

admin.site.register(TaggedItem)
admin.site.register(Tag, TagAdmin)
