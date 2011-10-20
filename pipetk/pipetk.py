#!/usr/bin/python
# -*- coding:Utf-8 -*-

import sys
import traceback
import re

class PipeTemplate(object):
    FAIL_ON_EXCEPTION = False
    DISPLAY_ERROR = True
    RETRY = False
    MAX_RETRY = 3
    UNMODIFIED_TO_STDOUT_ON_FAIL = False
    WITH_ENDL = True

    def __init__(self):
        pass

    def run(self):
        try:
            self.loop()
        except KeyboardInterrupt:
            sys.exit(0)

    def process(self, line):
        raise NotImplemented

    def loop(self):
        line = sys.stdin.readline()
        while line:
            self.iter(line, 0)
            line = sys.stdin.readline()

    def iter(self, line, number_of_retry):
        try:
            for result in self.process(line):
                if self.WITH_ENDL:
                    sys.stdout.write("%s\n" % result)
                else:
                    sys.stdout.write("%s" % result)
                sys.stdout.flush()
        except IOError:
            sys.exit(1)
        except Exception, e:
            if self.FAIL_ON_EXCEPTION:
                raise e
            if self.DISPLAY_ERROR:
                traceback.print_exc(file=sys.stderr)
                sys.stderr.write("%s\n" % e)
            if self.RETRY and number_of_retry < self.MAX_RETRY:
                self.iter(line, number_of_retry + 1)

class URLPipeTemplate(PipeTemplate):
    WITH_EXTRA_SPACE=False

    def process(self, line):
        if self.WITH_EXTRA_SPACE:
            yield re.sub('https?://[^ ]+ ?', self._process_url, line[:-1])
        else:
            yield re.sub('https?://[^ ]+', self._process_url, line[:-1])

    def _process_url(self, url):
        url = url.group()
        try:
            return self.process_url(url)
        except Exception, e:
            if self.FAIL_ON_EXCEPTION:
                raise e
            if self.DISPLAY_ERROR:
                traceback.print_exc(file=sys.stderr)
                sys.stderr.write("%s\n" % e)
            return url

    def process_url(self, url):
        raise NotImplemented

if __name__ == "__main__":
    pass

# vim:set shiftwidth=4 tabstop=4 expandtab:
