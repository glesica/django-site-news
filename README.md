Django-site-news Readme
=======================
Django-site-news is a small Django app for including site updates, status and
other news on the front page (or anywhere, really) of a web site.

Author
------
George Lesica <glesica@gmail.com>

Installing
----------
  1. Put the app somewhere in your `PYTHONPATH`.
  2. Add `site_news` to `INSTALLED_APPS`.
  3. Set values for the necessary settings (see below).
  4. Run a `./manage.py syncdb`. This should install a fixture (see Using).

Settings
--------
  * `MAX_SITE_NEWS_ITEMS` (required) - the maximum number of news items that 
    will ever be displayed. If the number of active items (in the correct date 
    range) is greater than this, items that started displaying longer ago will 
    be dropped. Set to `0` for no limit.
  * `MIN_SITE_NEWS_CATEGORY` (required) - similar to the Django message 
    framework. Categories that have their `weight` set below this number will 
    not be displayed. This can be used to display test messages on a staging 
    or development server but have them hidden in production.

Using
-----
There is a fixture included that will populate three default categories. Of 
course these can be ignored or even deleted but they should be acceptable for 
many sites.

Along with these categories there are also three constants corresponding to 
the weight of each of the categories in `site_news.constants`. These can be 
used to set `MIN_SITE_NEWS_CATEGORY`. These can be ignored as well.

The first thing you'll want to do is check out the categories to see if the 
defaults meet your needs.

Once you've done that, create a test news item on your development or staging 
server and insert it into your project.

You can do this one of two ways. The first is to simply use the included 
template tag to generate all the necessary markup for you. In your template:

    {% load site_news %}
    <html>
    <head>
        <title>My Awesome Site</title>
    </head>
    <body>
        {% site_news %}
        <p>...</p>
    </body>
    </html>

The second way to insert site news items is to use the included context 
processor. Add `site_news.context_processors.site_news` to your 
`TEMPLATE_CONTEXT_PROCESSORS` setting.

Then, in your templates (assuming you are using a `RequestContext`) you 
will have access to a variable called `site_news_items`. Iterating through 
it will give you each valid and current news item. In your template:

    <html>
    <head>
        <title>My Awesome Site</title>
    </head>
    <body>
        {% for item in site_news_items %}
            <div class="{{ item.category.css }}">
                <h3>{{ item.title }}</h3>
                <p>{{ item.content }}</p>
            </div>
        {% empty %}
            <p>No news today!</p>
        {% endfor %}
    </body>
    </html>
