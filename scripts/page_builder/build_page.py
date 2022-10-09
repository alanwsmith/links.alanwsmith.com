#!/usr/bin/env python3

import json

from string import Template

with open('config.json') as _json:
    config = json.load(_json)
    print(config)

# with open('template.html') as _template:
#     template = Template(_template.read())
#     output = template.substitute(
#         name="Karl",
#         color="Green"
#     )
#     print(output)

