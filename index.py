#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import cgi
import cgitb
import sqlite3
import os
import sys
cgitb.enable()

from my_db import *
from my_html import *
from my_speciality import *
from my_author import *
from my_study_form import *
from my_discipline import *
from my_material import *

uipage_case = { "material": material_showui, "authors": authors_showui, "discipline": discipline_showui, "speciality": speciality_showui, "study_form": study_form_showui }


form = cgi.FieldStorage()

if "page" in form:
	page = form.getfirst("page","")
	if page in uipage_case:
		uipage_case[page](form)
		exit(0)
	else:
		uipage_case["material"](None)
		exit(0)
else:
	uipage_case["material"](None)
	exit(0)

