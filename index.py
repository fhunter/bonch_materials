#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import bottle
from bottle import route, view, request, template, static_file, response, abort, redirect
import sqlite3
import os
import sys

from my_db import *
from my_study_form import *
from my_speciality import *
from my_discipline import *
from my_author import *
from my_material import *

#Materials
#TODO
@route('/')
@route('/materials')
@view('materials')
def materials():
	result=get_materials()
	result1 = []
	for i in result:
		authors_table = template('vtable', data = i[6], 
			headers = (u"ФИО",),
			width = (False,))
		belongs_table = template('vtable', data = i[7], 
			headers = (u"Специальность","Год","Форма обучения","Дисциплина","Семестр"),
			width = (False,False,False,False,False),)
		files_table =   template('vtable', data = i[8],
			headers = (u"Имя","Размер",),
			width = (False,False,),)
		j = (i[0],i[1],i[2],i[3],i[4],i[5],authors_table,belongs_table,files_table)
		result1.append(j)
	#uuid, name, description, owner, upload_date, edit_date, authors, course_belongs, files
	return dict(data = result1, headers = (u"Название",u"Описание",u"Владелец",u"Дата заливки",u"Дата редактирования",u"Авторы",u"Принадлежность",u"Файлы",), width=(False,True,False,False,False,False,False,False,),)

@route('/materials/delete/<uuid>')
def materials_delete(uuid):
	del_material(uuid)
	redirect("../../materials")

#TODO
@route('/materials/edit/<uuid>')
@view('materials_edit')
def materials_edit(uuid):
	result=get_material(uuid)
	result1 = []
	authors_table = template('vtable', data = result[6], 
		headers = (u"ФИО",),
		width = (False,))
	belongs_table = template('vtable', data = result[7], 
		headers = (u"Специальность","Год","Форма обучения","Дисциплина","Семестр"),
		width = (False,False,False,False,False),)
	files_table =   template('vtable', data = result[8],
		headers = (u"Имя","Размер",),
		width = (False,False,),)
	j = (result[0],result[1],result[2],result[3],result[4],result[5],authors_table,belongs_table,files_table)
	result1.append(j)
	return dict(data = result1, headers = (u"Название",u"Описание",u"Владелец",u"Дата заливки",u"Дата редактирования",u"Авторы",u"Принадлежность",u"Файлы",), width=(False,True,False,False,False,False,False,False,), uuid = result[0])

@route('/materials/edit/<uuid>/author/del/<uuida>')
def materials_delete_author(uuid,uuida):
	del_author(uuid,uuida)
	redirect("../../../../../materials")

@route('/materials/edit/<uuid>/author/add/<uuida>')
def materials_delete_author(uuid,uuida):
	add_author(uuid,uuida)
	redirect("../../../../../materials")

#TODO
@route('/materials/edit/<uuid>',method='POST')
@view('materials_edit')
def materials_edit_post(uuid):
	#name = request.forms.get("materials_name", None)
	redirect("../../materials")

#TODO
@route('/materials/add')
@view('materials_edit')
def materials_add():
	return dict(action = "add", uuid = "", button = "Добавить",)

#TODO
@route('/materials/add', method='POST')
def materials_add_post():
	redirect("../materials")

#Authors
@route('/authors')
@view('authors')
def authors():
	result=get_authors()
	return dict(data = result, headers = (u"ФИО автора",), width = (False,))

@route('/authors/delete/<uuid>')
def authors_delete(uuid):
	db_exec_sql("delete from authors where uuid = ?", (uuid,))
	redirect("../../authors")

@route('/authors/edit/<uuid>')
@view('authors_edit')
def authors_edit(uuid):
	author = db_exec_sql("select uuid, fio from authors where uuid = ?", (uuid,))
	author= author[0]
	return dict(uuid = author[0], fio = author[1])

@route('/authors/edit/<uuid>',method='POST')
@view('authors_edit')
def authors_edit_post(uuid):
	name = request.forms.get("authors_name", None)
	if name:
		db_exec_sql("update authors set fio= ? where uuid = ?", (name.decode('utf-8'), uuid,))
	redirect("../../authors")

@route('/authors/add')
@view('authors_edit')
def authors_add():
	return dict(fio = "", action = "add", uuid = "", button = "Добавить")

@route('/authors/add', method='POST')
def authors_add_post():
	authors_name = request.forms.get("authors_name", None)
	if authors_name:
		db_exec_sql("insert into authors (uuid, fio) select *, ? from next_uuid", (str(authors_name).decode('utf-8'),))
	redirect("../authors")

#Discipline
@route('/discipline')
@view('discipline')
def discipline():
	result=get_discipline()
	return dict(data = result, headers = (u"Название",u"Семестр",u"Описание"), width = (False,False,True))

@route('/discipline/delete/<uuid>')
def discipline_delete(uuid):
	db_exec_sql("delete from discipline where uuid = ?", (uuid,))
	redirect("../../discipline")

@route('/discipline/edit/<uuid>')
@view('discipline_edit')
def discipline_edit(uuid):
	discipline = db_exec_sql("select uuid, name, description,semester from discipline where uuid = ?", (uuid,))[0]
	return dict(uuid = discipline[0], name = discipline[1], description = discipline[2], semester = discipline[3])

@route('/discipline/edit/<uuid>',method='POST')
@view('discipline_edit')
def discipline_edit_post(uuid):
	name = request.forms.get("discipline_name", None)
	semester = request.forms.get("discipline_code", None)
	description = request.forms.get("discipline_description", None)
	if name:
		db_exec_sql("update discipline set name= ? where uuid = ?", (name.decode('utf-8'), uuid,))
	if semester:
		db_exec_sql("update discipline set semester= ? where uuid = ?", (semester.decode('utf-8'), uuid,))
	if description:
		db_exec_sql("update discipline set description= ? where uuid = ?", (description.decode('utf-8'), uuid,))
	redirect("../../discipline")

@route('/discipline/add')
@view('discipline_edit')
def discipline_add():
	return dict(name = "", semester = "", description = "", action = "add", uuid = "", button = "Добавить")

@route('/discipline/add', method='POST')
def discipline_add_post():
	name = request.forms.get("discipline_name", None)
	semester = request.forms.get("discipline_semester", None)
	description = request.forms.get("discipline_description", None)
	if name and semester:
		db_exec_sql("insert into discipline (uuid, name, semester, description) select *, ?, ?, ? from next_uuid", (str(name).decode('utf-8'),str(semester).decode('utf-8'),str(description).decode('utf-8'),))
	redirect("../discipline")


#Speciality
@route('/speciality')
@view('speciality')
def speciality():
	result=get_speciality()
	return dict(data = result, headers = (u"Шифр",u"Название",u"Описание"), width=(False,False,True))

@route('/speciality/delete/<uuid>')
def speciality_delete(uuid):
	db_exec_sql("delete from speciality where uuid = ?", (uuid,))
	redirect("../../speciality")

@route('/speciality/edit/<uuid>')
@view('speciality_edit')
def speciality_edit(uuid):
	speciality = db_exec_sql("select uuid, name, code, description from speciality where uuid = ?", (uuid,))[0]
	return dict(uuid = speciality[0], name = speciality[1], code = speciality[2], description = speciality[3])

@route('/speciality/edit/<uuid>',method='POST')
@view('speciality_edit')
def speciality_edit_post(uuid):
	name = request.forms.get("speciality_name", None)
	code = request.forms.get("speciality_code", None)
	description = request.forms.get("speciality_description", None)
	if name:
		db_exec_sql("update speciality set name= ? where uuid = ?", (name.decode('utf-8'), uuid,))
	if code:
		db_exec_sql("update speciality set code= ? where uuid = ?", (code.decode('utf-8'), uuid,))
	if description:
		db_exec_sql("update speciality set description= ? where uuid = ?", (description.decode('utf-8'), uuid,))
	redirect("../../speciality")

@route('/speciality/add')
@view('speciality_edit')
def speciality_add():
	return dict(name = "", code = "", description = "", action = "add", uuid = "", button = "Добавить")

@route('/speciality/add', method='POST')
def speciality_add_post():
	name = request.forms.get("speciality_name", None)
	code = request.forms.get("speciality_code", None)
	description = request.forms.get("speciality_description", None)
	if name and code:
		db_exec_sql("insert into speciality (uuid, name, code, description) select *, ?, ?, ? from next_uuid", (str(name).decode('utf-8'),str(code).decode('utf-8'),str(description).decode('utf-8'),))
	redirect("../speciality")

#Study form
@route('/study_form')
@view('study_form')
def study_form():
	result=get_study_form()
	return dict(data = result, headers = (u"Форма обучения",), width=(False,))

@route('/study_form/delete/<uuid>')
def study_form_delete(uuid):
	db_exec_sql("delete from study_form where uuid = ?", (uuid,))
	redirect("../../study_form")

@route('/study_form/edit/<uuid>')
@view('study_form_edit')
def study_form_edit(uuid):
	material = db_exec_sql("select uuid, study_form from study_form where uuid = ?", (uuid,))
	material= material[0]
	return dict(uuid = material[0], name = material[1])

@route('/study_form/edit/<uuid>',method='POST')
@view('study_form_edit')
def study_form_edit_post(uuid):
	new_name = request.forms.get("study_form_name", None)
	if new_name:
		name = new_name
		db_exec_sql("update study_form set study_form= ? where uuid = ?", (name.decode('utf-8'), uuid,))
	redirect("../../study_form")

@route('/study_form/add')
@view('study_form_edit')
def study_form_add():
	return dict(name = "", action = "add", uuid = "", button = "Добавить")

@route('/study_form/add', method='POST')
def study_form_add_post():
	name = request.forms.get("study_form_name", None)
	if name:
		db_exec_sql("insert into study_form (uuid, study_form) select *, ? from next_uuid", (str(name).decode('utf-8'),))
	redirect("../study_form")


#This is access for our css file
@route('/<filename:re:.*\.css>')
def send_image(filename):
	return static_file(filename, root='./files/', mimetype='text/css')

#This is files for material access
@route('/materials/<filename:re:.*>')
def send_image(filename):
	return static_file(filename, root='./')

bottle.run(server=bottle.CGIServer) 
