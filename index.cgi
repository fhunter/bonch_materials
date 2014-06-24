#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import cgi
import cgitb
import json
import sqlite3

cgitb.enable()

def db_open():
	conn = sqlite3.connect("materials.sqlite")
	conn.execute('pragma foreign_keys = on')
	return conn

def header_html():
        print "Content-type: text/html"
        print ""

def header_txt():
        print "Content-type: text/plain"
        print ""

def print_ui(page):
        print """<html><head><meta http-equiv="Content-Type" content="text/html;charset=utf8"></head><body>
	<link rel="stylesheet" type="text/css" href="style.css" /><title>Система управления учебными материалами</title>"""
        print page.encode('utf-8')
	print """</body></html>"""

def get_materials():
	conn = db_open()
	cursor = conn.cursor()
	cursor.execute("select uuid, name,description,owner, upload_date, edit_date from materials")
	result=cursor.fetchall()
	conn.close()
	return result

def get_discipline():
	conn = db_open()
	cursor = conn.cursor()
	cursor.execute("select uuid, name,semester,description from discipline")
	result = cursor.fetchall()
	conn.close()
	return result

def get_authors():
	conn = db_open()
	cursor = conn.cursor()
	cursor.execute("select uuid, fio from authors")
	result=cursor.fetchall()
	conn.close()
	return result

def get_study_form():
	conn = db_open()
	cursor = conn.cursor()
	cursor.execute("select uuid, study_form from study_form")
	result=cursor.fetchall()
	conn.close()
	return result

def get_speciality():
	conn = db_open()
	cursor = conn.cursor()
	cursor.execute("select uuid, code, name, description from speciality")
	result=cursor.fetchall()
	conn.close()
	return result

def get_belongs(uuid):
	conn = db_open()
	cursor = conn.cursor()
	cursor.execute("select authorship.author_uuid, authors.fio from authorship,authors where authorship.material_uuid = ? and authors.uuid = authorship.author_uuid", (uuid,))
	result = cursor.fetchall()
	return result

def insert_delete_btn(uuid, func_name):
	text =  u""
	text += u"<div class=\"delete_button\"><button onClick=\"javascript:%s('%s')\">Удалить</button></div></div>" % (func_name, uuid,)
  	return text

def gen_table_row(name, value ):
	text = u"<tr><td class=field_name>%s</td><td class=field_value>%s</td></tr>" % (name, value, )
	return text

def gen_table_row_wide( name, value ):
	text = u"<tr><td class=field_name>%s</td></tr><tr><td class=field_value colspan=2>%s</td></tr>" %( name, value, )
	return text


main_page=u"""
    <div id="container">
      <div id="header">
	<h1>Система управления учебными материалами</h1>
      </div>
      <div id="menu">
	<a href="./?material=show">  <button>Материалы</button></a>
	<a href="./?authors=show">   <button>Авторы</button></a>
	<a href="./?discipline=show"><button>Дисциплины</button></a>
	<a href="./?speciality=show"><button>Специальности</button></a>
	<a href="./?study_form=show"><button>Формы обучения</button></a>
      </div>
      <div id="UI_elements">

	<div id="material_admin" class="UI_tab" >
	  <h2>Учебные материалы, список</h2>
	  <div class="add_form">
	  <form id="material_add_form" action="javascript:add_material()">
	    <input id="material_name">
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

authors_page=u"""
    <div id="container">
      <div id="header">
	<h1>Система управления учебными материалами</h1>
      </div>
      <div id="menu">
	<a href="./?material=show">  <button>Материалы</button></a>
	<a href="./?authors=show">   <button>Авторы</button></a>
	<a href="./?discipline=show"><button>Дисциплины</button></a>
	<a href="./?speciality=show"><button>Специальности</button></a>
	<a href="./?study_form=show"><button>Формы обучения</button></a>
      </div>
      <div id="UI_elements">

	<div id="author_admin" class="UI_tab" >
	  <h2>Управление списком авторов</h2>
	  <div class="add_form">
	  <form id="author_add_form" action="javascript:add_author()">
	    <input id="authors_name">
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

discipline_page=u"""
    <div id="container">
      <div id="header">
	<h1>Система управления учебными материалами</h1>
      </div>
      <div id="menu">
	<a href="./?material=show">  <button>Материалы</button></a>
	<a href="./?authors=show">   <button>Авторы</button></a>
	<a href="./?discipline=show"><button>Дисциплины</button></a>
	<a href="./?speciality=show"><button>Специальности</button></a>
	<a href="./?study_form=show"><button>Формы обучения</button></a>
      </div>
      <div id="UI_elements">

	<div id="discipline_admin" class="UI_tab" >
	  <h2>Управление списком дисциплин</h2>
	  <div class="add_form">
	  <form id="discipline_add_form" action="javascript:add_discipline()">
	    Название:<input id="discipline_name"><br>
	    Семестр:<input id="discipline_semester"><br>
	    Описание:<br>
	    <textarea id="discipline_description"></textarea>
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

speciality_page=u"""
    <div id="container">
      <div id="header">
	<h1>Система управления учебными материалами</h1>
      </div>
      <div id="menu">
	<a href="./?material=show">  <button>Материалы</button></a>
	<a href="./?authors=show">   <button>Авторы</button></a>
	<a href="./?discipline=show"><button>Дисциплины</button></a>
	<a href="./?speciality=show"><button>Специальности</button></a>
	<a href="./?study_form=show"><button>Формы обучения</button></a>
      </div>
      <div id="UI_elements">
	<div id="speciality_admin" class="UI_tab" >
	  <h2>Управление списком специальностей</h2>
	  <div class="add_form">
	  <form id="speciality_add_form" action="javascript:add_speciality()">
	    Шифр:<input id="speciality_code"><br>
	    Название:<input id="speciality_name"><br>
	    Описание<br>
	    <textarea id="speciality_description"></textarea><br>
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

study_form_page=u"""
    <div id="container">
      <div id="header">
	<h1>Система управления учебными материалами</h1>
      </div>
      <div id="menu">
	<a href="./?material=show">  <button>Материалы</button></a>
	<a href="./?authors=show">   <button>Авторы</button></a>
	<a href="./?discipline=show"><button>Дисциплины</button></a>
	<a href="./?speciality=show"><button>Специальности</button></a>
	<a href="./?study_form=show"><button>Формы обучения</button></a>
      </div>
      <div id="UI_elements">
	  <div id="study_form_admin" class="UI_tab" >
	  <h2>Управление списком форм обучения</h2>
	  <div class="add_form">
	  <form id="study_form_add_form" action="javascript:add_study_form()">
	    <input id="study_form_name">
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

if "material" in form:
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
		table += insert_delete_btn(i[0], "delete_material")
	page = main_page % (table, )
	print_ui(page )
	exit(0)
if "authors" in form:
	header_html()
	result = get_authors()
	table = u""
	for i in result:
		table += "<div class=\"list_element\">"
		table += "<table>"
		table += gen_table_row( u"ФИО автора", i[1] )
		table += "</table>"
		table += insert_delete_btn( i[0], "author=delete")
	page = authors_page % (table, )
	print_ui(page)
	exit(0)
if "study_form" in form:
	header_html()
	result=get_study_form()
	table = u""
	for i in result:
		table+=u"<div class=\"list_element\"><table>"
		table+=gen_table_row(u"Форма обучения", i[1])
		table+=u"</table>";
		table+=insert_delete_btn(i[0],"study_form=delete")
	page = study_form_page % (table, )
	print_ui(page)
	exit(0)
if "discipline" in form:
	header_html()
	result=get_discipline()
	table = u""
	for i in result:
		table += "<div class=\"list_element\">"
		table += "<table>"
		table += gen_table_row( u"Название", i[1] )
		table += gen_table_row( u"Семестр", i[2] )
		table += gen_table_row_wide( u"Описание", i[3] )
		table += "</table>"
		table += insert_delete_btn( i[0], "discipline=delete" )
	page = discipline_page % (table, )
	print_ui(page)
	exit(0)
if "speciality" in form:
	header_html()
	result=get_speciality()
	table = u""
	for i in result:
		table += u"<div class=\"list_element\"><table>"
		table += gen_table_row( u"Шифр", i[1] )
		table += gen_table_row( u"Название", i[2] )
		table += gen_table_row_wide( u"Описание", i[3] );
		table += "</table>";
		table += insert_delete_btn( i[0], "speciality=delete" );
	page = speciality_page % (table, )
	print_ui(page)
	exit(0)
header_html()
print_ui(main_page )
exit(0)





#	if form["query"].value == "add_material":
#		print_header()
#		print "Здесь должна быть заливка и проверка материалов"
#	if form["query"].value == "delete_material":
#		print_header()
#		print "Здесь должно быть удаление материалов"
#	if form["query"].value == "add_discipline":
#		if "name" in form and "sem" in form:
#			conn = db_open()
#			cursor = conn.cursor()
#			t1 = form["name"].value
#			t2 = form["sem"].value
#			if "desc" in form:
#				t3 = form["desc"].value
#			else:
#				t3 = ""
#			cursor.execute("insert into discipline (uuid, name, semester, description) select *, ?, ?, ? from next_uuid", (str(t1).decode('utf-8'),str(t2).decode('utf-8'),str(t3).decode('utf-8'),))
#			conn.commit()
#			js=json.dumps({"error": 0, "discipline": cursor.fetchall()})
#			conn.close()
#			print_header()
#			print js
#		else:
#			print_header()
#			print json.dumps({"error": 1 })
#	if form["query"].value == "delete_discipline":
#		if "uuid" in form:
#			conn = db_open()
#			cursor = conn.cursor()
#			t = form["uuid"].value
#			cursor.execute("delete from discipline where uuid = ?", (t,))
#			conn.commit()
#			js=json.dumps({"error": 0, "discipline": cursor.fetchall()})
#			conn.close()
#			print_header()
#			print js
#		else:
#			print_header()
#			print json.dumps({"error": 1 })
#	if form["query"].value == "add_author":
#		if "fio" in form:
#			conn = db_open()
#			cursor = conn.cursor()
#			t = form["fio"].value
#			cursor.execute("insert into authors (uuid, fio) select *, ? from next_uuid", (str(t).decode('utf-8'),))
#			conn.commit()
#			js=json.dumps({"error": 0, "authors": cursor.fetchall()})
#			conn.close()
#			print_header()
#			print js
#		else:
#			print_header()
#			print json.dumps({"error": 1 })
#	if form["query"].value == "delete_author":
#		if "uuid" in form:
#			conn = db_open()
#			cursor = conn.cursor()
#			t = form["uuid"].value
#			cursor.execute("delete from authors where uuid = ?", (t,))
#			conn.commit()
#			js=json.dumps({"error": 0, "authors": cursor.fetchall()})
#			conn.close()
#			print_header()
#			print js
#		else:
#			print_header()
#			print json.dumps({"error": 1 })
#	if form["query"].value == "add_speciality":
#		if "name" in form and "code" in form:
#			conn = db_open()
#			cursor = conn.cursor()
#			t1 = form["name"].value
#			t2 = form["code"].value
#			if "desc" in form:
#				t3 = form["desc"].value
#			else:
#				t3 = ""
#			cursor.execute("insert into speciality (uuid, name, code, description) select *, ?, ?, ? from next_uuid", (str(t1).decode('utf-8'),str(t2).decode('utf-8'),str(t3).decode('utf-8'),))
#			conn.commit()
#			js=json.dumps({"error": 0, "speciality": cursor.fetchall()})
#			conn.close()
#			print_header()
#			print js
#		else:
#			print_header()
#			print json.dumps({"error": 1 })
#	if form["query"].value == "delete_speciality":
#		if "uuid" in form:
#			conn = db_open()
#			cursor = conn.cursor()
#			t = form["uuid"].value
#			cursor.execute("delete from speciality where uuid = ?", (t,))
#			conn.commit()
#			js=json.dumps({"error": 0, "speciality": cursor.fetchall()})
#			conn.close()
#			print_header()
#			print js
#		else:
#			print_header()
#			print json.dumps({"error": 1 })
#	if form["query"].value == "add_study_form":
#		if "name" in form:
#			conn = db_open()
#			cursor = conn.cursor()
#			t = form["name"].value
#			cursor.execute("insert into study_form (uuid, study_form) select *, ? from next_uuid", (str(t).decode('utf-8'),))
#			conn.commit()
#			js=json.dumps({"error": 0, "study_form": cursor.fetchall()})
#			conn.close()
#			print_header()
#			print js
#		else:
#			print_header()
#			print json.dumps({"error": 1 })
#	if form["query"].value == "delete_study_form":
#		if "uuid" in form:
#			conn = db_open()
#			cursor = conn.cursor()
#			t = form["uuid"].value
#			cursor.execute("delete from study_form where uuid = ?", (t,))
#			conn.commit()
#			js=json.dumps({"error": 0, "study_form": cursor.fetchall()})
#			conn.close()
#			print_header()
#			print js
#		else:
#			print_header()
#			print json.dumps({"error": 1 })
#	if form["query"].value == "add_belongs":
#		print_header()
#		print "Здесь должна быть обработка принадлежности"
#	if form["query"].value == "delete_belongs":
#		print_header()
#		print "Здесь должна быть обработка удаления принадлежности"
