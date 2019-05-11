from .get_tag_html import get_tag_html
from .get_header_html import get_header_html
from .get_footer_html import get_footer_html


def get_form_html(html):
    html = html.replace(get_header_html(html), "")
    html = html.replace(get_footer_html(html), "")
    noscript_html = get_tag_html(
        html,
        "<noscript class=\"ninja-forms-noscript-message\">",
        "</noscript>"
    )
    html = html.replace(noscript_html, "")
    div_html = get_tag_html(html, "<div>", "</div>")
    html = html.replace(div_html, "")
    script_html = get_tag_html(html, "<script>", "</script>")
    html = html.replace(script_html, "")
    return "{}{}{}".format(noscript_html, div_html, script_html)
