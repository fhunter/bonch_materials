#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import bottle
from bottle import route, view, request, template, static_file, response, abort
import sqlite3
import os
import sys

from my_db import *

@route('/')
@route('/materials')
@view('materials')
def materials():
	return dict()

@route('/authors')
@view('authors')
def authors():
	return dict()

@route('/discipline')
@view('discipline')
def discipline():
	return dict()

@route('/speciality')
@view('speciality')
def speciality():
	return dict()

@route('/study_form')
@view('study_form')
def study_form():
	return dict()

@route('/<filename:re:.*\.css>')
def send_image(filename):
    return static_file(filename, root='./files/', mimetype='text/css')

bottle.run(server=bottle.CGIServer) 
