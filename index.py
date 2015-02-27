#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import bottle
from bottle import route, view, request, template, static_file, response, abort
import sqlite3
import os
import sys

from my_db import *
from my_study_form import *
from my_speciality import *
from my_discipline import *
from my_author import *
from my_material import *

@route('/')
@route('/materials')
@view('materials')
def materials():
	result=get_materials()
	return dict(data = result)

@route('/authors')
@view('authors')
def authors():
	result=get_authors()
	return dict(data = result, headers = (u"ФИО автора",), width = (False,))

@route('/authors/delete/<uuid>')
def author_delete(uuid):
	return ""

@route('/discipline')
@view('discipline')
def discipline():
	result=get_discipline()
	return dict(data = result, headers = (u"Название",u"Семестр",u"Описание"), width = (False,False,True))

@route('/speciality')
@view('speciality')
def speciality():
	result=get_speciality()
	return dict(data = result, headers = (u"Шифр",u"Название",u"Описание"), width=(False,False,True))

@route('/study_form')
@view('study_form')
def study_form():
	result=get_study_form()
	return dict(data = result, headers = (u"Форма обучения",), width=(False,))

@route('/study_form/delete/<uuid>')
def study_form_delete(uuid):
	return ""

@route('/study_form/edit/<uuid>')
def study_form_edit(uuid):
	return ""

@route('/study_form/edit/<uuid>',method='POST')
def study_form_edit_post(uuid):
	return ""

@route('/study_form/add')
def study_form_add():
	return ""


#This is access for our css file
@route('/<filename:re:.*\.css>')
def send_image(filename):
	return static_file(filename, root='./files/', mimetype='text/css')

#This is files for material access
@route('/materials/<filename:re:.*>')
def send_image(filename):
	return static_file(filename, root='./')

bottle.run(server=bottle.CGIServer) 
