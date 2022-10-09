#!/usr/bin/env python3

import json

from string import Template


link_templates = {
    'main':  Template("""
<dt>
<h4><a href="$URL">$NAME</a></h4>
<div class="url_display"><a href="$URL">$URL_DISPLAY</a></div>
</dt>
<dd>
$DESCRIPTION
</dd>
"""),

    'links_page':  Template("""
<dt>
<h4>$NAME &lt- You Are Here</h4>
<div class="url_display">$URL_DISPLAY</div>
</dt>
<dd>
$DESCRIPTION
</dd>
"""),

    'strike':  Template("""
<dt>
<h4><strike>$NAME</strike></h4>
<div class="url_display"><strike>$URL_DISPLAY</strike></div>
</dt>
<dd>
$DESCRIPTION
</dd>
""")

}


with open('config.json') as _json:
    config = json.load(_json)
    links = config['links']
    links.sort(key=lambda x: x['name'].lower().replace('the ', ''))
    html_links = []
    for link in links:
        if 'type' not in link:
            html_links.append(link_templates['main'].substitute(
                NAME=link['name'],
                URL=link['url'],
                URL_DISPLAY=link['display_url'],
                DESCRIPTION=f"<p>{'</p><p>'.join(link['description'])}</p>"
            ))
        else:
            html_links.append(link_templates[link['type']].substitute(
                NAME=link['name'],
                URL=link['url'],
                URL_DISPLAY=link['display_url'],
                DESCRIPTION=f"<p>{'</p><p>'.join(link['description'])}</p>"
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

