#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import cgi
import cgitb
import json
import sqlite3

cgitb.enable()

def print_header():
	print "Content-type: text/javascript"
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
	if form["query"].value == "courses":
		conn = sqlite3.connect("materials.sqlite")
		cursor = conn.cursor()
		cursor.execute("select uuid, name from courses")
		js=json.dumps({"error": 0, "courses": cursor.fetchall()})
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
		print_header()
		print "Здесь должно быть удаление курсов"
	if form["query"].value == "add_course":
		if "name" in form:
			conn = sqlite3.connect("materials.sqlite")
			cursor = conn.cursor()
			t = form["name"].value
			cursor.execute("insert into courses (uuid, name) select *, ? from next_uuid", (t,))
			conn.commit()
			js=json.dumps({"error": 0, "courses": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "add_belongs":
		print_header()
		print "Здесь должна быть обработка принадлежности"
	if form["query"].value == "delete_belongs":
		print_header()
		print "Здесь должна быть обработка удаления принадлежности"
