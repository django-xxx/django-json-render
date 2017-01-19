# -*- coding: utf-8 -*-

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render


def json_render(request, template_name, dictionary=None):
    return render(request, template_name, {
        'data': json.dumps(dictionary or {}, cls=DjangoJSONEncoder)
    })
