#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import cgi
import cgitb
import json
import sqlite3

cgitb.enable()

def print_header():
	print "Content-type: text/javascript; charset=utf-8"
	print ""

form = cgi.FieldStorage()
if "query" not in form:
	print json.dumps({"error": 1 });
else:
	if form["query"].value == "materials":
		conn = sqlite3.connect("materials.sqlite")
		cursor = conn.cursor()
		cursor.execute("select uuid, name from materials")
		js=json.dumps({"error": 0, "materials": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "discipline":
		conn = sqlite3.connect("materials.sqlite")
		cursor = conn.cursor()
		cursor.execute("select uuid, name from discipline")
		js=json.dumps({"error": 0, "discipline": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "authors":
		conn = sqlite3.connect("materials.sqlite")
		cursor = conn.cursor()
		cursor.execute("select uuid, fio from authors")
		js=json.dumps({"error": 0, "authors": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "speciality":
		conn = sqlite3.connect("materials.sqlite")
		cursor = conn.cursor()
		cursor.execute("select uuid, code, name from speciality")
		js=json.dumps({"error": 0, "speciality": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "study_form":
		conn = sqlite3.connect("materials.sqlite")
		cursor = conn.cursor()
		cursor.execute("select uuid, study_form from study_form")
		js=json.dumps({"error": 0, "study_form": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "add_material":
		print_header()
		print "Здесь должна быть заливка и проверка материалов"
	if form["query"].value == "delete_material":
		print_header()
		print "Здесь должно быть удаление материалов"
	if form["query"].value == "delete_course":
		if "uuid" in form:
			conn = sqlite3.connect("materials.sqlite")
			cursor = conn.cursor()
			t = form["uuid"].value
			cursor.execute("delete from courses where uuid = ?", (t,))
			conn.commit()
			js=json.dumps({"error": 0, "courses": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "add_course":
		if "name" in form:
			conn = sqlite3.connect("materials.sqlite")
			cursor = conn.cursor()
			t = form["name"].value
			cursor.execute("insert into courses (uuid, name) select *, ? from next_uuid", (str(t).decode('utf-8'),))
			conn.commit()
			js=json.dumps({"error": 0, "courses": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "add_discipline":
		print_header()
		print "Здесь должна быть обработка дисциплины"
	if form["query"].value == "delete_discipline":
		print_header()
		print "Здесь должна быть обработка удаления дисциплины"
	if form["query"].value == "add_author":
		print_header()
		print "Здесь должна быть обработка автора"
	if form["query"].value == "delete_author":
		print_header()
		print "Здесь должна быть обработка удаления автора"
	if form["query"].value == "add_speciality":
		print_header()
		print "Здесь должна быть обработка специальности"
	if form["query"].value == "delete_speciality":
		print_header()
		print "Здесь должна быть обработка удаления специальности"
	if form["query"].value == "add_study_form":
		print_header()
		print "Здесь должна быть обработка формы обучения"
	if form["query"].value == "delete_study_form":
		print_header()
		print "Здесь должна быть обработка удаления формы обучения"
	if form["query"].value == "add_belongs":
		print_header()
		print "Здесь должна быть обработка принадлежности"
	if form["query"].value == "delete_belongs":
		print_header()
		print "Здесь должна быть обработка удаления принадлежности"
