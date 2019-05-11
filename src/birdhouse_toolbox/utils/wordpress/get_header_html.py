def get_header_html(html, closing_tag="</p>"):
    closing_tag_start = html.find(closing_tag)
    closing_tag_end = closing_tag_start + len(closing_tag)
    result = html[0:closing_tag_end]
    return result
