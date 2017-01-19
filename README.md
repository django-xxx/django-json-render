# django-json-render
Django JSON Render

## Installation
```shell
pip install django-json-render
```

## Usage
```python
from json_render import json_render

def xxx(request):
    return json_render(request, template_name, dictionary)
    
# Render in template
window.RenderModel = {{ data|safe }}
```
