def get_footer_html(html, opening_tag="<p>"):
    opening_tag_start = html.rfind(opening_tag)
    opening_tag_end = opening_tag_start + len(opening_tag)
    closing_tag = opening_tag.replace("<", "</")
    closing_tag_start = html.rfind(closing_tag)
    closing_tag_end = closing_tag_start + len(closing_tag)
    result = html[opening_tag_start:closing_tag_end]
    return result
