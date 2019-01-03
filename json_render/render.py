# -*- coding: utf-8 -*-

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render


def json_render(request, template_name, dictionary=None, unjsondumpsdict=None,
                setcookie=False, delcookie=False, signedcookie=True, cookie_key=None, cookie_value=None, cookie_salt=None,
                cookie_max_age=None, cookie_expires=None, cookie_path='/', cookie_domain=None, cookie_secure=False, cookie_httponly=False, ignore_blank=False):

    unjsondumpsdict = unjsondumpsdict or {}
    unjsondumpsdict['data'] = json.dumps(dictionary or {}, cls=DjangoJSONEncoder)

    response = render(request, template_name, unjsondumpsdict)

    if setcookie:
        if ignore_blank and not cookie_value:
            return response

        if signedcookie:
            response.set_signed_cookie(cookie_key, cookie_value, salt=cookie_salt, **{
                'max_age': cookie_max_age,
                'expires': cookie_expires,
                'path': cookie_path,
                'domain': cookie_domain,
                'secure': cookie_secure,
                'httponly': cookie_httponly,
            })
        else:
            response.set_cookie(cookie_key, cookie_value, max_age=cookie_max_age, expires=cookie_expires, path=cookie_path, domain=cookie_domain, secure=cookie_secure, httponly=cookie_httponly)

    if delcookie:
        response.delete_cookie(cookie_key)

    return response
