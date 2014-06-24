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
        print """<html><head><meta http-equiv="Content-Type" content="text/html;charset=utf8"></head><body>"""
        print page.encode('utf-8')
	print """</body></html>"""

mainpage=u"""
    <div id="container">
      <div id="header">
	<h1>Система управления учебными материалами</h1>
      </div>
      <div id="menu">
	<button onClick="div_toggle('material_admin');">Материалы</button>
	<button onClick="div_toggle('author_admin');">Авторы</button>
	<button onClick="div_toggle('discipline_admin');">Дисциплины</button>
	<button onClick="div_toggle('speciality_admin');">Специальности</button>
	<button onClick="div_toggle('study_form_admin');">Формы обучения</button>
      </div>
      <div id="UI_elements">

	<div id="material_admin" class="UI_tab" style="display: inline">
	  <h2>Учебные материалы, список</h2>
	  <div class="add_form">
	  <form id="material_add_form" action="javascript:add_material()">
	    <input id="material_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <button onClick="load_materials();">Обновить</button>
	  </div>
	  <div id="material_list" class="UI_list">
	  </div>
	</div>

	<div id="author_admin" class="UI_tab" style="display: none">
	  <h2>Управление списком авторов</h2>
	  <div class="add_form">
	  <form id="author_add_form" action="javascript:add_author()">
	    <input id="authors_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <button onClick="load_authors();">Обновить</button>
	  </div>
	  <div id="author_list" class="UI_list">
	  </div>
	</div>

	<div id="discipline_admin" class="UI_tab" style="display: none">
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
	  <button onClick="load_disciplines();">Обновить</button>
	  </div>
	  <div id="discipline_list" class="UI_list">
	  </div>
	</div>

	<div id="speciality_admin" class="UI_tab" style="display: none">
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
	  <button onClick="load_specialities();">Обновить</button>
	  </div>
	  <div id="speciality_list" class="UI_list">
	  </div>
	</div>

	<div id="study_form_admin" class="UI_tab" style="display: none">
	  <h2>Управление списком форм обучения</h2>
	  <div class="add_form">
	  <form id="study_form_add_form" action="javascript:add_study_form()">
	    <input id="study_form_name">
	    <input type=submit value="Добавить">
	  </form>
	  </div>
	  <div class="refresh_button">
	  <button onClick="load_study_forms();">Обновить</button>
	  </div>
	  <div id="study_form_list" class="UI_list">
	  </div>
	</div>

      </div>
    </div>
"""

header_html()
print_ui(mainpage)
