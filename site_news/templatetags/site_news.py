from datetime import datetime

from django import template
from django.conf import settings

from site_news.models import SiteNewsItem

def site_news():
    """
    Inserts the currently active news items into the page.
    """
    # Grab all active items in proper date/time range.
    items = SiteNewsItem.current_and_active.all()
    
    # Take only the number requested.
    max_items = settings.MAX_SITE_NEWS_ITEMS
    if max_items > 0:
        items = items[:max_items]
    
    return {'items': items}

register = template.Library()
register.inclusion_tag('site_news/news.html')(site_news)
