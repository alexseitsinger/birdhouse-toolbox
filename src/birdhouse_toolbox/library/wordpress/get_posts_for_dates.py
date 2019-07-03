import maya

from .get_posts import get_posts


def get_posts_for_dates(site_url, start_date, end_date):
    # get the posts
    posts_all = []
    posts_selected = []
    pages_tried_max = 100
    done = False
    for i in list(range(1, pages_tried_max + 1)):
        if done is True:
            continue
        try:
            posts = get_posts(site_url, page_number=i)
            posts_all.extend(posts)
        except Exception as exc:
            done = True
    for post in posts_all:
        post_date = maya.when(post["date"], timezone="UTC")
        if post_date >= start_date and post_date <= end_date:
            posts_selected.append(post)
    return posts_selected
