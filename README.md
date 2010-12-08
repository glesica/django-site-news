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
  4. Run a `./manage.py syncdb`.

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
