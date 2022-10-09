#!/usr/bin/env python3

import json

from string import Template

link_template = Template("""
<dt>
<h4><a href="$URL">$NAME</a></h4>
<div class="url_display"><a href="$URL">$URL_DISPLAY</a></div>
</dt>
<dd>
$DESCRIPTION
</dd>
""")

with open('config.json') as _json:
    config = json.load(_json)
    links = config['links']
    links.sort(key=lambda x: x['name'].lower())
    html_links = []
    for link in links:
        html_links.append(link_template.substitute(
            NAME=link['name'],
            URL=link['url'],
            URL_DISPLAY=link['display_url'],
            DESCRIPTION=link['description']
        ))
    
    with open('template.html') as _template:
        template = Template(_template.read())
        with open('../../site/index.html', 'w') as _output:
            _output.write(template.substitute(
                DETAILS="".join(html_links)
            ))






# with open('template.html') as _template:
#     template = Template(_template.read())
#     output = template.substitute(
#         name="Karl",
#         color="Green"
#     )
#     print(output)

