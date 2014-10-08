#!/usr/bin/python
# Filename: build_multipart_form_data.py

import hashlib
import datetime

def build_multipart_form_data(fields):
    boundary = hashlib.md5(str(datetime.datetime.now())).hexdigest();
    data = '';
    for field in fields:
        #add boundary
        data += "--%s\r\n" % boundary
        # add headers
        for key, value in field['headers'].iteritems():
            data += "%s:%s\r\n" %(key, value)
        # add blank line
        data += "\r\n"
        # add body
        data += "%s\r\n" %field['body']
    # add closing boundary if there were fields
    if data:
        data += "%s--%s--\r\n" %(data, boundary)
    return boundary, data