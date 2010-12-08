from django.contrib import admin

from site_news.models import SiteNewsItem, SiteNewsCategory

admin.site.register(SiteNewsItem)
admin.site.register(SiteNewsCategory)
