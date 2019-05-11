import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE_NAME = os.path.basename(ROOT_DIR)
RE_VARIABLE = r"{} = ['\"]([^'\"]*)['\"]"


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

