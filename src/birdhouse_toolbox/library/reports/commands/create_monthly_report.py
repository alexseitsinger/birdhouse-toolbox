from ...wordpress.get_posts_for_dates import get_posts_for_dates
from ...get_dates_for_duration import get_dates_for_duration


def create_monthly_report(site_url, month, year):
    """
    1) Add opening summary.
        1a) List posts published.
        1b) Include any custom actvity performed.
    3) Add website performance.
        3a) Create comparison in traffic for dates from last month.
        3b) Add measurements of traffic for dates of posts.
        3c) Add measurements for forms completed and leads generated.
    4) Add email performance.
        4a) Add number of contacts emailed.
        4b) Add links clicked.
    5) Add social media performance.
        5a) For each post, add:
            5a1) Total reach
            5a2) Total links clicked
    6) Add closing notes.
    """
    start_date_str = "{}/1/{}".format(month, year)
    start_date, end_date = get_dates_for_duration(start_date_str, months=1)
    posts = get_posts_for_dates(site_url, start_date=start_date, end_date=end_date)
    # add summary of posts to beginning of report.
    # add custom message to beinginning of report.
    # get google analytics for dates
    # create comparison in traffic from last month.
    # measure traffic on dates of posts.
    # add forms completed and leads generated.
    # get email analytics for dates.
    # add email metrics to report.
    # add social media perforamance metrics.
    # add closing notes.
    return posts
