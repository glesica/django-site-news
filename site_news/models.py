from django.db import models

from site_news.managers import SiteNewsItemManager

class SiteNewsItem(models.Model):
    """
    A single news item.
    """
    title = models.CharField(
        max_length=140,
    )
    content = models.TextField(
        blank=True,
        null=True,
        help_text='A message associated with this item.',
    )
    active = models.BooleanField(
        default=False,
        help_text='Only active news items will ever be displayed.',
    )
    start = models.DateTimeField(
        help_text='The earliest date/time this item should be displayed.',
    )
    end = models.DateTimeField(
        help_text='The latest date/time this item should be displayed.',
    )
    category = models.ForeignKey(
        'SiteNewsCategory',
    )
    objects = models.Manager()
    current_and_active = SiteNewsItemManager()
    
    class Meta:
        ordering = ['-start', 'title']
        get_latest_by = 'start'
        verbose_name = 'News Item'
        verbose_name_plural = 'News Items'
        
    def __unicode__(self):
        return self.title


class SiteNewsCategory(models.Model):
    """
    A category for site news items.
    """
    name = models.CharField(
        max_length=140,
        help_text='Category name will be listed when creating a news item.',
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text='Describe the category. For reference only. Optional.',
    )
    weight = models.IntegerField(
        unique=True,
        help_text='You can set the minimum weight to display in settings. This number much be unique.',
    )
    css = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        help_text='Extra CSS class that will be added to items of this category.',
    )
    
    class Meta:
        ordering = ['weight']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.name
