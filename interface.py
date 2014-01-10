#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import cgi
import cgitb
import json
import sqlite3

cgitb.enable()

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
		print js
	if form["query"].value == "courses":
		conn = sqlite3.connect("materials.sqlite")
		cursor = conn.cursor()
		cursor.execute("select uuid, name from courses")
		js=json.dumps({"error": 0, "courses": cursor.fetchall()})
		conn.close()
		print js
	if form["query"].value == "add_material":
		print "Здесь должна быть заливка и проверка материалов"
	if form["query"].value == "delete_material":
		print "Здесь должно быть удаление материалов"
	if form["query"].value == "delete_course":
		print "Здесь должно быть удаление курсов"
	if form["query"].value == "add_course":
		print "Здесь должно быть добавление курсов"
	if form["query"].value == "add_belongs":
		print "Здесь должна быть обработка принадлежности"
	if form["query"].value == "delete_belongs":
		print "Здесь должна быть обработка удаления принадлежности"
