from django.conf import settings

from site_news.models import SiteNewsItem

def site_news(request):
    """
    Inserts the currently active news items into the template context.
    
    This ignores MAX_SITE_NEWS_ITEMS.
    """
    # Grab all active items in proper date/time range.
    items = SiteNewsItem.current_and_active.all()
    
    return {'site_news_items': items}
