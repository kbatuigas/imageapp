from django import template

import base64

register = template.Library()


@register.filter
def bin_to_img(_bin):
    if _bin is not None:
        return base64.b64encode(_bin).decode('utf-8')