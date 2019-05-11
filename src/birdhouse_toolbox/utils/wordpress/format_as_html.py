import re
import itertools


def to_html(tag_name, content):
    opening_tag = "<{}>".format(tag_name)
    closing_tag = "</{}>".format(tag_name)
    content = content.strip()
    return "{}{}{}".format(opening_tag, content, closing_tag)


def is_list_item(text):
    m = re.match(r"^[\d\w]\.", text)
    try:
        m.group()
        return True
    except AttributeError:
        return False


def create_item_list(sections, index):
    item_list = []
    start = index + 2
    end = len(sections) - 1
    items = sections[start:end]
    for item in items:
        if not len(item.strip()):
            break
        item_index = sections.index(item)
        if is_list_item(item):
            item_list.append(create_item_list(sections, item_index))
        else:
            item_list.append(item_index)
    return item_list


def create_html_list(sections, item_list, tag_name="ol"):
    first = item_list[0]
    last = item_list[-1]
    opening_tag = "<{}>".format(tag_name)
    closing_tag = "</{}>".format(tag_name)
    sections[first] = opening_tag + sections[first]
    sections[last] = sections[last] + closing_tag


def format_as_html(text):
    sections = text.strip().split("\n")
    title_index = 0
    title = sections.pop(title_index)
    cta_index = -3
    cta = sections.pop(cta_index)
    item_lists = []
    paragraph_list = []
    for section in sections:
        if len(section.strip()):
            index = sections.index(section)
            if section.endswith(":"):
                item_lists.append(create_item_list(sections, index))
            indexes = list(itertools.chain.from_iterable(item_lists))
            if index not in indexes:
                paragraph_list.append(index)
    for index in paragraph_list:
        sections[index] = to_html("p", sections[index])
    for item_list in item_lists:
        for index in item_list:
            sections[index] = to_html("li", sections[index])
    for item_list in item_lists:
        create_html_list(sections, item_list)
    sections.insert(cta_index + 1, to_html("h3", cta))
    sections.insert(title_index, to_html("h2", title))
    return "".join(sections)
