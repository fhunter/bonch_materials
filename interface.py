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
		conn.execute('pragma foreign_keys = on')
		cursor = conn.cursor()
		cursor.execute("select uuid, name,description,owner, upload_date, edit_date from materials")
		js=json.dumps({"error": 0, "materials": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "author_for_material":
		if "uuid" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t1 = form["uuid"].value
			cursor.execute("select author_uuid from authorship where material_uuid = ?", (t1,))
			conn.commit()
			js=json.dumps({"error": 0, "belongs": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "discipline":
		conn = sqlite3.connect("materials.sqlite")
		conn.execute('pragma foreign_keys = on')
		cursor = conn.cursor()
		cursor.execute("select uuid, name,semester,description from discipline")
		js=json.dumps({"error": 0, "discipline": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "authors":
		conn = sqlite3.connect("materials.sqlite")
		conn.execute('pragma foreign_keys = on')
		cursor = conn.cursor()
		cursor.execute("select uuid, fio from authors")
		js=json.dumps({"error": 0, "authors": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "speciality":
		conn = sqlite3.connect("materials.sqlite")
		conn.execute('pragma foreign_keys = on')
		cursor = conn.cursor()
		cursor.execute("select uuid, code, name, description from speciality")
		js=json.dumps({"error": 0, "speciality": cursor.fetchall()})
		conn.close()
		print_header()
		print js
	if form["query"].value == "study_form":
		conn = sqlite3.connect("materials.sqlite")
		conn.execute('pragma foreign_keys = on')
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
	if form["query"].value == "add_discipline":
		if "name" in form and "sem" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t1 = form["name"].value
			t2 = form["sem"].value
			if "desc" in form:
				t3 = form["desc"].value
			else:
				t3 = ""
			cursor.execute("insert into discipline (uuid, name, semester, description) select *, ?, ?, ? from next_uuid", (str(t1).decode('utf-8'),str(t2).decode('utf-8'),str(t3).decode('utf-8'),))
			conn.commit()
			js=json.dumps({"error": 0, "discipline": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "delete_discipline":
		if "uuid" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t = form["uuid"].value
			cursor.execute("delete from discipline where uuid = ?", (t,))
			conn.commit()
			js=json.dumps({"error": 0, "discipline": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "add_author":
		if "fio" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t = form["fio"].value
			cursor.execute("insert into authors (uuid, fio) select *, ? from next_uuid", (str(t).decode('utf-8'),))
			conn.commit()
			js=json.dumps({"error": 0, "authors": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "delete_author":
		if "uuid" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t = form["uuid"].value
			cursor.execute("delete from authors where uuid = ?", (t,))
			conn.commit()
			js=json.dumps({"error": 0, "authors": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "add_speciality":
		if "name" in form and "code" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t1 = form["name"].value
			t2 = form["code"].value
			if "desc" in form:
				t3 = form["desc"].value
			else:
				t3 = ""
			cursor.execute("insert into speciality (uuid, name, code, description) select *, ?, ?, ? from next_uuid", (str(t1).decode('utf-8'),str(t2).decode('utf-8'),str(t3).decode('utf-8'),))
			conn.commit()
			js=json.dumps({"error": 0, "speciality": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "delete_speciality":
		if "uuid" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t = form["uuid"].value
			cursor.execute("delete from speciality where uuid = ?", (t,))
			conn.commit()
			js=json.dumps({"error": 0, "speciality": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "add_study_form":
		if "name" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t = form["name"].value
			cursor.execute("insert into study_form (uuid, study_form) select *, ? from next_uuid", (str(t).decode('utf-8'),))
			conn.commit()
			js=json.dumps({"error": 0, "study_form": cursor.fetchall()})
			conn.close()
			print_header()
			print js
		else:
			print_header()
			print json.dumps({"error": 1 })
	if form["query"].value == "delete_study_form":
		if "uuid" in form:
			conn = sqlite3.connect("materials.sqlite")
			conn.execute('pragma foreign_keys = on')
			cursor = conn.cursor()
			t = form["uuid"].value
			cursor.execute("delete from study_form where uuid = ?", (t,))
			conn.commit()
			js=json.dumps({"error": 0, "study_form": cursor.fetchall()})
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
