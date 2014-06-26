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


def get_materials():
	result = db_exec_sql("select uuid, name,description,owner, upload_date, edit_date from materials")
	return result

def material_showui(form):
	header_html()
	result=get_materials()
	table = u""
	for i in result:
		table += "<div class=\"list_element\">"
		table += "<table>"
		table += gen_table_row( u"Название" , i[1])
		table += gen_table_row( u"Дата заливки" , i[4])
		if i[5] == None:
			table += gen_table_row( u"Дата редактирования" , u"Никогда")
		else:
			table += gen_table_row( u"Дата редактирования" , i[5])
		table += gen_table_row( u"Заливал", i[3])
		tmp = get_belongs(i[0])
		for j in tmp:
			table += gen_table_row( u"Автор", j[1])
		table += gen_table_row_wide( u"Описание", i[2])
		table += "</table>"
		table += insert_edit_delete_btn(i[0], "delete_material")
	page = main_page % (table, )
	print_ui(page )


def get_discipline():
	result = db_exec_sql("select uuid, name,semester,description from discipline")
	return result

def add_discipline(name,semester,description):
	db_exec_sql("insert into discipline (uuid, name, semester, description) select *, ?, ?, ? from next_uuid", (str(name).decode('utf-8'),str(semester).decode('utf-8'),str(description).decode('utf-8'),))

def del_discipline(uuid):
	db_exec_sql("delete from discipline where uuid = ?", (uuid,))

def discipline_showui(form):
	header_html()
	if is_post():
		if ("discipline_name" in form) and ("discipline_semester" in form):
			discipline_name = cgi.escape(form.getfirst("discipline_name",""))
			discipline_semester = cgi.escape(form.getfirst("discipline_semester",""))
			discipline_description = cgi.escape(form.getfirst("discipline_description",""))
			add_discipline(discipline_name,discipline_semester,discipline_description)
		if "uuid" in form:
			uuid = cgi.escape(form.getfirst("uuid",""))
			del_discipline(uuid)
	result=get_discipline()
	table = gen_table(result, (u"Название",u"Семестр",u"Описание"),(False,False,True))
	page = discipline_page % (table, )
	print_ui(page)

def get_authors():
	result = db_exec_sql("select uuid, fio from authors")
	return result

def add_authors(name):
	db_exec_sql("insert into authors (uuid, fio) select *, ? from next_uuid", (str(name).decode('utf-8'),))

def del_authors(uuid):
	db_exec_sql("delete from authors where uuid = ?", (uuid,))

def authors_showui(form):
	header_html()
	if is_post():
		if "authors_name" in form:
			authors_name = cgi.escape(form.getfirst("authors_name",""))
			add_authors(authors_name)
		if "uuid" in form:
			uuid = cgi.escape(form.getfirst("uuid",""))
			del_authors(uuid)
	result = get_authors()
	table = gen_table(result, (u"ФИО автора",),(False,))
	page = authors_page % (table, )
	print_ui(page)

def get_study_form():
	result = db_exec_sql("select uuid, study_form from study_form")
	return result

def add_study_form(name):
	db_exec_sql("insert into study_form (uuid, study_form) select *, ? from next_uuid", (str(name).decode('utf-8'),))

def del_study_form(uuid):
	db_exec_sql("delete from study_form where uuid = ?", (uuid,))

def study_form_showui(form):
	header_html()
	if is_post():
		if "study_form_name" in form:
			study_form_name = cgi.escape(form.getfirst("study_form_name",""))
			add_study_form(study_form_name)
		if "uuid" in form:
			uuid = cgi.escape(form.getfirst("uuid",""))
			del_study_form(uuid)
	result=get_study_form()
	table = gen_table(result, (u"Форма обучение",),(False,))
	page = study_form_page % (table, )
	print_ui(page)
	

def get_belongs(uuid):
	result = db_exec_sql("select authorship.author_uuid, authors.fio from authorship,authors where authorship.material_uuid = ? and authors.uuid = authorship.author_uuid", (uuid,))
	return result

uipage_case = { "material": material_showui, "authors": authors_showui, "discipline": discipline_showui, "speciality": speciality_showui, "study_form": study_form_showui }

main_page= header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="material_admin" class="UI_tab" >
	  <h2>Учебные материалы, список</h2>
	  <div class="add_form">
	  <form id="material_add_form" method="post" action="">
	    <input name="material_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?material=show">  <button>Обновить</button></a>
	  </div>
	  <div id="material_list" class="UI_list">
	  %s
	  </div>
	</div>
	</div>
	</div>
	"""

authors_page=header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="author_admin" class="UI_tab" >
	  <h2>Управление списком авторов</h2>
	  <div class="add_form">
	  <form id="author_add_form" method="post" action="">
	    <input name="authors_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?authors=show">  <button>Обновить</button></a>
	  </div>
	  <div id="author_list" class="UI_list">
	  %s
	  </div>
	</div>
	</div>
	</div>
	"""

discipline_page=header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="discipline_admin" class="UI_tab" >
	  <h2>Управление списком дисциплин</h2>
	  <div class="add_form">
	  <form id="discipline_add_form" method="post" action="">
	    Название:<input name="discipline_name"><br>
	    Семестр:<input name="discipline_semester"><br>
	    Описание:<br>
	    <textarea name="discipline_description"></textarea>
	    <br>
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?discipline=show">  <button>Обновить</button></a>
	  </div>
	  <div id="discipline_list" class="UI_list">
	  %s
	  </div>
	</div>
	</div>
	</div>
	"""

speciality_page=header_include + menu_include + u"""
      <div id="UI_elements">
	<div id="speciality_admin" class="UI_tab" >
	  <h2>Управление списком специальностей</h2>
	  <div class="add_form">
	  <form id="speciality_add_form" method="post" action="">
	    <input type="hidden" name="action" value="add"/>
	    Шифр:<input name="speciality_code"><br>
	    Название:<input name="speciality_name"><br>
	    Описание<br>
	    <textarea name="speciality_description"></textarea><br>
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?speciality=show">  <button>Обновить</button></a>
	  </div>
	  <div id="speciality_list" class="UI_list">
	  %s
	  </div>
	</div>
	</div>
	</div>
	"""

study_form_page=header_include + menu_include + u"""
      <div id="UI_elements">
	  <div id="study_form_admin" class="UI_tab" >
	  <h2>Управление списком форм обучения</h2>
	  <div class="add_form">
	  <form id="study_form_add_form" method="post" action="">
	    <input name="study_form_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <a href="./?study_form=show">  <button>Обновить</button></a>
	  </div>
	  <div id="study_form_list" class="UI_list">
	  %s
	  </div>
	</div>

      </div>
    </div>
"""

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

