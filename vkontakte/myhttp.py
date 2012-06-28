#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2


def post(url, data, headers, timeout):
    http = httplib2.Http(timeout=timeout)
    response, content = http.request(url, 'POST', headers=headers, body=data)
    return response.status, content
