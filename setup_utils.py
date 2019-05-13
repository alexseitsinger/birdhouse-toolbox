import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE_NAME = os.path.basename(ROOT_DIR)
RE_VARIABLE = r"{} = ['\"]([^'\"]*)['\"]"
RE_README_SECTION_HEADING = r"#+ {}"
RE_README_SECTION = r"{}[^#]*"


def read_section(path=("README.md",), title="Description", sentences=(0,)):
    content = read(path)
    heading = RE_README_SECTION_HEADING.format(title)
    section_regex = RE_README_SECTION.format(heading)
    match = re.search(section_regex, content)
    try:
        desc = match.group(0)
        desc = desc.strip()
        desc = re.sub(r"{}\n+".format(heading), "", desc)
        parts = desc.split(".")
        desc = ". ".join([x for x in parts if parts.index(x) in sentences])
        desc = desc.strip()
    except AttributeError:
        desc = ""
    return desc


def read(parts, variable=None):
    with open(os.path.join(ROOT_DIR, *parts), 'r', encoding='utf-8') as f:
        content = f.read()
    if variable is None:
        return content
    regex = RE_VARIABLE.format(variable)
    match = re.search(regex, content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Failed to read {} variable".format(variable))

