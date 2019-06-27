def get_tag_html(html, opening_tag, closing_tag):
    opening_tag_start = html.find(opening_tag)
    opening_tag_end = opening_tag_start + len(opening_tag)
    closing_tag_start = html.find(closing_tag)
    closing_tag_end = closing_tag_start + len(closing_tag)
    return html[opening_tag_start:closing_tag_end]
