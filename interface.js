function div_toggle(div_id){
  var t=document.getElementById(div_id);
  for(i=0;i<t.parentElement.getElementsByTagName("div").length;i++){
    p=t.parentElement.getElementsByTagName("div")[i];
    if(p.parentElement.id == t.parentElement.id ){
      if(p.id==div_id){
	p.style.display ="inline";
      }else{
	p.style.display ="none";
      }
    }
  }
}

function add_material(){
}

function add_author(){
  var jsonHttp = null;
  var name = document.getElementById("authors_name").value;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=add_author&fio="+name, false );
  jsonHttp.send( null );
  load_authors()
}

function add_speciality(){
  var jsonHttp = null;
  var name = document.getElementById("speciality_name").value;
  var code = document.getElementById("speciality_code").value;
  var desc = document.getElementById("speciality_description").value;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=add_speciality&name="+name+"&code="+code+"&desc="+desc, false );
  jsonHttp.send( null );
  load_specialities()
}

function add_discipline(){
  var jsonHttp = null;
  var name = document.getElementById("discipline_name").value;
  var sem = document.getElementById("discipline_semester").value;
  var desc = document.getElementById("discipline_description").value;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=add_discipline&name="+name+"&sem="+sem+"&desc="+desc, false );
  jsonHttp.send( null );
  load_disciplines()
}

function add_study_form(){
  var jsonHttp = null;
  var name = document.getElementById("study_form_name").value;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=add_study_form&name="+name, false );
  jsonHttp.send( null );
  load_study_forms()
}

function delete_material(uuid){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=delete_material&uuid="+uuid, false );
  jsonHttp.send( null );
  load_materials()
}

function delete_author(uuid){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=delete_author&uuid="+uuid, false );
  jsonHttp.send( null );
  load_authors()
}

function delete_speciality(uuid){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=delete_speciality&uuid="+uuid, false );
  jsonHttp.send( null );
  load_specialities()
}

function delete_discipline(uuid){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=delete_discipline&uuid="+uuid, false );
  jsonHttp.send( null );
  load_disciplines()
}

function delete_study_form(uuid){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=delete_study_form&uuid="+uuid, false );
  jsonHttp.send( null );
  load_study_forms()
}

function data_load(){
  load_materials()
  load_authors()
  load_specialities()
  load_disciplines()
  load_study_forms()
}

function load_materials(){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=materials", false );
  jsonHttp.send( null );
  var myobject = JSON.parse(jsonHttp.responseText);
  var text = "";
  for(i=0;i<myobject.materials.length;i++){
    text += "<div class=\"list_element\">" + myobject.materials[i][1] + " - " + myobject.materials[i][2] + " - " + myobject.materials[i][3] + " - " + myobject.materials[i][4] + " - " + myobject.materials[i][5] + "<div class=\"delete_button\"><button onClick=\"javascript:delete_material('" + myobject.materials[i][0] + "')\">Удалить</button></div></div>";
//    load_belongs();
  };
  document.getElementById("material_list").innerHTML = text;
}

function load_authors(){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=authors", false );
  jsonHttp.send( null );
  var myobject = JSON.parse(jsonHttp.responseText);
  var text = "";
  for(i=0;i<myobject.authors.length;i++){
    text += "<div class=\"list_element\">"+ myobject.authors[i][1] + "<div class=\"delete_button\"><button onClick=\"javascript:delete_author('" + myobject.authors[i][0] + "')\">Удалить</button></div></div>";
//    load_belongs();
  };
  document.getElementById("author_list").innerHTML = text;
}

function load_specialities(){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=speciality", false );
  jsonHttp.send( null );
  var myobject = JSON.parse(jsonHttp.responseText);
  var text = "";
  for(i=0;i<myobject.speciality.length;i++){
    text += "<div class=\"list_element\">";
    text += "<table><tr><td>Шифр</td><td>" + myobject.speciality[i][1] +"<td>Название</td><td>"+ myobject.speciality[i][2] + "</td></tr>";
    text += "<tr><td>Описание</td></tr>";
    text += "<tr><td>" + myobject.speciality[i][3] + "</td></tr>";
    text += "</table>";
    text += "<div class=\"delete_button\"><button onClick=\"javascript:delete_speciality('" + myobject.speciality[i][0] + "')\">Удалить</button></div></div>";
//    load_belongs();
  };
  document.getElementById("speciality_list").innerHTML = text;
}

function load_disciplines(){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=discipline", false );
  jsonHttp.send( null );
  var myobject = JSON.parse(jsonHttp.responseText);
  var text = "";
  for(i=0;i<myobject.discipline.length;i++){
    text += "<div class=\"list_element\">"+ myobject.discipline[i][1] +" = "+ myobject.discipline[i][2] + " = " + myobject.discipline[i][3] + "<div class=\"delete_button\"><button onClick=\"javascript:delete_discipline('" + myobject.discipline[i][0] + "')\">Удалить</button></div></div>";
//    load_belongs();
  };
  document.getElementById("discipline_list").innerHTML = text;
}

function load_study_forms(){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=study_form", false );
  jsonHttp.send( null );
  var myobject = JSON.parse(jsonHttp.responseText);
  var text = "";
  for(i=0;i<myobject.study_form.length;i++){
    text += "<div class=\"list_element\">"+ myobject.study_form[i][1] + "<div class=\"delete_button\"><button onClick=\"javascript:delete_study_form('" + myobject.study_form[i][0] + "')\">Удалить</button></div></div>";
//    load_belongs();
  };
  document.getElementById("study_form_list").innerHTML = text;
}
