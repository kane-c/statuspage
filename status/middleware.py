from __future__ import unicode_literals


class XForwardedForMiddleware():
    """
    Use this when running behind an nginx reverse proxy so Django knows the real
    IP. Otherwise REMOTE_ADDR will always be 127.0.0.1 (nginx) and not the
    user's IP.
    """
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR'].split(',', 1)[0]
            del request.META['HTTP_X_FORWARDED_FOR']

        return None
