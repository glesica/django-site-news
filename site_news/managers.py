from datetime import datetime

from django.db import models
from django.conf import settings

class SiteNewsItemManager(models.Manager):
    """
    Custom manager for news items. Allows all valid (active and in the right 
    time frame) items to be grabbed easily.
    """
    def get_query_set(self):
        min_category = settings.MIN_SITE_NEWS_CATEGORY
        return super(SiteNewsItemManager, self).get_query_set().filter(
            start__gt=datetime.now,
            end__lt=datetime.now,
            active=True,
            category__weight__gte=min_category,
        )
