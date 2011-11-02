Pipe Tool Kit
=============

This tool kit is an attempt to compile a set of tools I've created to solve
problems for La Quadrature du Net. Those tools are designed to works with unix
shell pipe. They follow the unix philosophy and aim to stay simple.

I'm going to try to keep them at least a bit documented but since I'm always in
an hurry I can't guaranteed this will always be the case.

You can have an idea of the power of this kind of problems solving approach
here: http://blog.worlddomination.be/projects/ungarage.html (this tuto doesn't
features those tools for the moment).

For organisation reason all the commands starts with the letter "p".

There is place for a lots of ameliorations, most of those tools are very
simplistic and could be generalised (for example pdetinyfy or purltitle could
be apply to each urls of a sentence, purls could use regex and could be
generalised for anything by accepting regex as an argument).

It's possible I'm reinventing the wheel for some of those commands. Don't
hesitate to tell me if it's the case.

Current tools
=============

* pipetk: list the available commands with the informations bellow.

* puniq: eliminate duplications in real time via a shell unix pipe.(| sort |
  uniq waits for the full stream to be completed and also sort it, therefor it,
  for example, won't works between a rsstail|feedstail and an ii file).
  Example:

  ::

    $ feedstail -u http://reddit.com/.rss | puniq

* pmerge: open a named pipe and write to stdout everything written in the named
  pipe. The first argument given is the name of the named pipe. It doesn't
  managed in any way the possible conflicts between multiple process that write
  on that pipe at the same time.
  Silly example:

  ::

    $ pmerge PIPE > irc.freenode.net/#laquadrature & echo "pouet" > PIPE

* purls: really simple url extracting tools. It split each line it receives by
  white space then display on a new line each words that starts with either
  "http" or "https".
  Example:

  ::

    $ echo "there is 2 urls in this sentence: this one http://blog.worlddomination.be and this one http://laquadrature.net" | purls
    http://blog.worlddomination.be
    http://laquadrature.net

* pdetinyfy: get the real url of a shortened url. FIXED: works on urls inside a string
  Example:

  ::

    $ echo "foo http://ur1.ca/4110r bar" | pdetinyfy
    foo http://laquadrature.net bar

* purltitle: get an url in input and output the url followed by it's title.
  FIXED: works on urls inside a string
  Example:

  ::

    $ echo "foo http://laquadrature.net bar" | purltitle
    foo http://laquadrature.net La Quadrature du Net | Internet et Libertés bar

* plag: slow down the displaying of a stream by sleeping a give time beetwen each line
  Can have the number of seconds the sleep as arg (accept float value).
  Example:

  ::

    dmseg | plag

  or:

  ::

    dmesg | plag 60

* puniqrt: try to avoid duplications of similar tweets. For example by removing
  RT tweets of a tweet that has already been displayed.
  Behave in the same way that puniq.

* premoveurls: remove the urls from a string. This is more an example script
  for the URLPipeTemplate class than something really usefull.
  Example:

  ::

    $ echo "foo http://laquadrature.net bar" | premoveurls
    "foo bar"


* cleanurls: clean urls by removing useless informations like tracking stuff
  like "?utm_*" args added to urls.

Coding new pipe utils
=====================

The PipeToolKit comes with 2 template python Class for coding new pipe
utilities for your need. Here are 2 simple example on how to use each ones. I
don't think that you'll need to now anything more. If you want to, just read
the code, it's not long.

PipeTemplate
------------

This is the standard template.

    ::

    from pipetk import PipeTemplate

    class Example(PipeTemplate):
        # Options: displayed here with their default value, you can change it by redefining it

        # FAIL_ON_EXCEPTION = False # define if the pipe will stop when an exception is raised

        # DISPLAY_ERROR = True # define if the exception backtrace and message are displayed

        # RETRY = False # define if the pipe must retry it's processing on an exception

        # MAX_RETRY = 3 # define the number of time the pipe must retry to process it's input on an exception

        # UNMODIFIED_TO_STDOUT_ON_FAIL = False # define if on an exception the unmodified text must be written

        # WITH_ENDL = True # define if the endl char must be sended to the process function

        def process(self, line):
            # called everytime a line is written on stdin, you must implement it

            # VERY IMPORTANT: process must return something iterable, either a

            # list or by being a decorator (by using yield). This allow you to

            # return severals different things.

            # do you stuff

            yield line

            # or

            return [a, b, c, d]

    if __name__ == "__main__":
        Example().run()

URLPipeTemplate
---------------

This is a template to work on every urls of a stream.

    ::

    from pipetk import URLPipeTemplate

    class Example(URLPipeTemplate):
        # Inherite from all the options of the PipeTemplate

        # Other option:

        # WITH_EXTRA_SPACE=False # define if the space that may follow the url in the string is send to the processing function

        # CAREFULL: this is process_URL, not process, you can't implement

        # process since it's already implemented to build this new template.

        def process_url(self, url):
            # called on every url encoutered

            # you must return a string

            return ""

    if __name__ == "__main__":
        Example().run()

More example?
-------------

Just read the code of the existing tools. Most of it are very simple.

Changelog
=========

0.2
---

* pdetinyfy now works for urls inside a string

* new script: puniqrt to try to eliminate duplications for tweets

* new template to build pipes utils that works on the urls of a string

* add premoveurls as en example script for the new template

* new script: pcleanurls to remove useless tracking pieces of urls (like utm_* stuff)

* various bug fixs

* add doc on how to write new pipe utils

0.1
---

* Init

Licence
=======

All those tools are released under the `GNU General Public License v3`_ or later.

.. _GNU General Public License v3 : http://www.gnu.org/licenses/gpl-3.0.html

Feedback
========

For any feedback you can contact me at <cortex at worlddomination dot be>.

Laurent Peuch
