==================
django-json-render
==================

Django JSON Render

Installation
============

::

    pip install django-json-render


Usage
=====

::

    from json_render import json_render

    def xxx(request):
        return json_render(request, template_name, dictionary)

    # Render in template
    window.RenderModel = {{ data|safe }}

