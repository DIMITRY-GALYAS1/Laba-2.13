# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun1(tag):
    def fun2(s):
        result = []
        result.append("<")
        result.append(tag)
        result.append(">")
        result.append(s)
        result.append("</")
        result.append(tag)
        result.append(">")
        return "".join(result)
    return fun2
