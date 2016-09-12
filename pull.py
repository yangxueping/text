#!/usr/bin/env python
# coding: utf-8

import os
from git import Repo

print "start..."

repo = Repo(os.getcwd())
if repo.remotes['origin']:
	origin = repo.remotes.origin
	origin.pull()
else:
	print "get pull error"

print "end..."