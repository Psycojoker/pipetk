Pipe Tool Kit
=============

This tool kit is an attempt to compile a set of tools I've created to solve
problems for La Quadrature du Net. Those tools are designed to works with unix
shell pipe. They follow the unix philosophy and aim to stay simple.

I'm going to try to keep them at least a bit documented but since I'm always in
an hurry I can't guaranteed this will always be the case.

You can have an idea of the power of this kind of problems solving approach
here: http://blog.worlddomination.be/microblogging/ (this tuto doesn't features
those tools for the moment).

For organisation reason all the commands starts with the letter "p".

There is place for a LOTS of ameliorations, most of those tools are very
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
  Example: feedstail -u http://reddit.com/.rss | puniq

* pmerge: open a named pipe and write to stdout everything written in the named
  pipe. The first argument given is the name of the named pipe. It doesn't
  managed in any way the possible conflicts between multiple process that write
  on that pipe at the same time.
  Silly example: pmerge PIPE > irc.freenode.net/#laquadrature & echo "pouet" > PIPE

* purls: really simple url extracting tools. It split each line it receives by
  white space then display on a new line each words that starts with either
  "http" or "https".
  Example: echo "there is 2 urls in this sentence: this one http://blog.worlddomination.be and this one http://laquadrature.net" | purls
  result:
  http://blog.worlddomination.be
  http://laquadrature.net

* pdetinyfy: get the real url of a shortened url. Works only by receiving one
  url per line.
  Example: echo "http://ur1.ca/4110r" | pdetinyfy
  Result: http://laquadrature.net
  echo "foo http://ur1.ca/4110r bar" | pdetinyfy <- won't work, use this instead:
  echo "foo http://ur1.ca/4110r bar" | purls | pdetinyfy

* purltitle: get an url in input and output the url followed by it's title.
  Works only by receiving one url per line. For the moment will miserably fail
  if it doesn't managed to connect to the website.
  Example: echo "http://laquadrature.net" | purltitle
  Result: http://laquadrature.net La Quadrature du Net | Internet et Libertés

Licence
=======
All those tools are released under the GPLv3+ licence.

Feedback
========
For any feedback you can contact me at cortex_AT_worlddomination_._be

Laurent Peuch
