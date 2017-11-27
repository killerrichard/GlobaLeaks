# -*- coding: utf-8 -*-
import os

from globaleaks.handlers.base import BaseHandler
from globaleaks.security import directory_traversal_check


class StaticFileHandler(BaseHandler):
    check_roles = '*'
    handler_exec_time_threshold = 30

    def __init__(self, state, request, path):
        BaseHandler.__init__(self, state, request)

        self.root = "%s%s" % (os.path.abspath(path), "/")

    def get(self, filename):
        if not filename:
            filename = 'index.html'

        abspath = os.path.abspath(os.path.join(self.root, filename))

        directory_traversal_check(self.root, abspath)

        return self.write_file(filename, abspath)


class AdminStaticFileHandler(StaticFileHandler):
    check_roles = 'admin'