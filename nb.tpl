{%- extends 'basic.tpl' -%}
{%- block header -%}
---
{% for k in nb.metadata.get("plotly") -%}
{%- if k == "permalink" -%}
permalink: {{ nb.metadata.get("plotly")[k].replace("python/", "python/next/") }}
{% elif k == "language" -%}
language: python/next
{% else -%}
{{ k }}: {{ nb.metadata.get("plotly")[k] }}
{% endif -%}
{%- endfor -%}
---
{{ super() }}
{{ '{% raw %}' }}
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.2/require.js"></script>

<div style="margin: 20px auto; width: 75%; background: #f4f4f8; padding: 20px; font-weight: 400; line-height: 1.85; text-align: center;">
	<strong>Note:</strong> this is <em>pre-release documentation</em> for the upcoming version 4 of Plotly.py.<br/>
	See our <a href="https://plot.ly/python/next/getting-started" style="color: #2391fe">Getting Started</a> guide for v4 installation instructions,
	or head on over to the <a href="https://plot.ly/python" style="color: #2391fe">current v3 docs</a>
</div>

{%- endblock header-%}


{%- block footer %}
{{ super() }}
{{ '{% endraw %}' }}
{%- endblock footer-%}
