#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import cgi
import cgitb
import json
import sqlite3

cgitb.enable()

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

main_page=u"""
    <div id="container">
      <div id="header">
	<h1>Система управления учебными материалами</h1>
      </div>
      <div id="menu">
	<a href="./?material=show">  <button>Материалы</button></a>
	<a href="./?authors=show">   <button>Авторы</button></a>
	<a href="./?study_form=show"><button>Дисциплины</button></a>
	<a href="./?discipline=show"><button>Специальности</button></a>
	<a href="./?speciality=show"><button>Формы обучения</button></a>
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
	<a href="./?study_form=show"><button>Дисциплины</button></a>
	<a href="./?discipline=show"><button>Специальности</button></a>
	<a href="./?speciality=show"><button>Формы обучения</button></a>
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
	<a href="./?study_form=show"><button>Дисциплины</button></a>
	<a href="./?discipline=show"><button>Специальности</button></a>
	<a href="./?speciality=show"><button>Формы обучения</button></a>
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
	<a href="./?study_form=show"><button>Дисциплины</button></a>
	<a href="./?discipline=show"><button>Специальности</button></a>
	<a href="./?speciality=show"><button>Формы обучения</button></a>
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
	<a href="./?study_form=show"><button>Дисциплины</button></a>
	<a href="./?discipline=show"><button>Специальности</button></a>
	<a href="./?speciality=show"><button>Формы обучения</button></a>
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
	  </div>
	</div>

      </div>
    </div>
"""

form = cgi.FieldStorage()

if "material" in form:
	header_html()
	print_ui(main_page)
	exit(0)
if "authors" in form:
	header_html()
	print_ui(authors_page)
	exit(0)
if "study_form" in form:
	header_html()
	print_ui(study_form_page)
	exit(0)
if "discipline" in form:
	header_html()
	print_ui(discipline_page)
	exit(0)
if "speciality" in form:
	header_html()
	print_ui(speciality_page)
	exit(0)
header_html()
print_ui(main_page)
exit(0)
