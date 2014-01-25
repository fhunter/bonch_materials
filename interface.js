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

function insert_delete_btn(uuid, func_name){
  var text = "";
  text += "<div class=\"delete_button\"><button onClick=\"javascript:";
  text += func_name;
  text += "('" + uuid + "')\">Удалить</button></div></div>";
  return text;
}

function fetch_json(request){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?" + request, false );
  jsonHttp.send( null );
  return JSON.parse(jsonHttp.responseText);
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
  var myobject = fetch_json("query=materials");
  var text = "";
  for(i=0;i<myobject.materials.length;i++){
    text += "<div class=\"list_element\">";
    text += "<table><tr>";
    text += "<td class=field_name>Название</td>";
    text += "<td class=field_value>" + myobject.materials[i][1] + "</td>";
    text += "</tr>";
    text += "<tr>";
    text += "<td class=field_name>Дата заливки</td>";
    text += "<td class=field_value>" + myobject.materials[i][4] + "</td>";
    text += "</tr>";
    text += "<tr>";
    text += "<td class=field_name>Дата редактирования</td>";
    if(myobject.materials[i][5]==null){
      text += "<td class=field_value>" + "Никогда" + "</td>";
    }else{
      text += "<td class=field_value>" + myobject.materials[i][5] + "</td>";
    }
    text += "</tr>";
    text += "<tr>";
    text += "<td class=field_name>Заливал</td>";
    text += "<td class=field_value>" + myobject.materials[i][3] + "</td>";
    text += "</tr>";
    text += "<tr><td class=field_name>Описание</td></tr>";
    text += "<tr><td class=field_value colspan=2>" + myobject.materials[i][2] + "</td></tr>";
    text += "</table>";
    text += insert_delete_btn(myobject.materials[i][0], "delete_material");
//    load_belongs();
  };
  document.getElementById("material_list").innerHTML = text;
}

function load_authors(){
  var myobject = fetch_json("query=authors");
  var text = "";
  for(i=0;i<myobject.authors.length;i++){
    text += "<div class=\"list_element\">";
    text += "<table><tr>";
    text += "<td class=field_name>ФИО автора</td>";
    text += "<td class=field_value>" + myobject.authors[i][1] + "</td>";
    text += "</tr></table>";
    text += insert_delete_btn( myobject.authors[i][0], "delete_author");
//    load_belongs();
  };
  document.getElementById("author_list").innerHTML = text;
}

function load_specialities(){
  var myobject = fetch_json("query=speciality");
  var text = "";
  for(i=0;i<myobject.speciality.length;i++){
    text += "<div class=\"list_element\">";
    text += "<table><tr>";
    text += "<td class=field_name>Шифр</td>";
    text += "<td class=field_value>" + myobject.speciality[i][1] + "</td>";
    text += "</tr>";
    text += "<tr>";
    text += "<td class=field_name>Название</td>";
    text += "<td class=field_value>"+ myobject.speciality[i][2] + "</td>";
    text += "</tr>";
    text += "<tr><td class=field_name>Описание</td></tr>";
    text += "<tr><td colspan=2 class=field_value>" + myobject.speciality[i][3] + "</td></tr>";
    text += "</table>";
    text += insert_delete_btn( myobject.speciality[i][0], "delete_speciality" );
//    load_belongs();
  };
  document.getElementById("speciality_list").innerHTML = text;
}

function load_disciplines(){
  var myobject = fetch_json("query=discipline");
  var text = "";
  for(i=0;i<myobject.discipline.length;i++){
    text += "<div class=\"list_element\">";
    text += "<table><tr>";
    text += "<td class=field_name>Название</td>"
    text += "<td class=field_value>" + myobject.discipline[i][1] + "</td>";
    text += "</tr>";
    text += "<tr>";
    text += "<td class=field_name>Семестр</td>";
    text += "<td class=field_value>"+ myobject.discipline[i][2] + "</td>";
    text += "</tr>";
    text += "<tr><td class=field_name>Описание</td></tr>";
    text += "<tr><td class=field_value colspan=2>" + myobject.discipline[i][3] + "</td></tr>";
    text += "</table>";
    text += insert_delete_btn( myobject.discipline[i][0], "delete_discipline" );
//    load_belongs();
  };
  document.getElementById("discipline_list").innerHTML = text;
}

function load_study_forms(){
  var myobject = fetch_json("query=study_form");
  var text = "";
  for(i=0;i<myobject.study_form.length;i++){
    text += "<div class=\"list_element\">";
    text += "<table><tr>";
    text += "<td class=field_name>Форма обучения</td>";
    text += "<td class=field_value>" + myobject.study_form[i][1] + "</td>";
    text += "</tr></table>";
    text += insert_delete_btn( myobject.study_form[i][0], "delete_study_form" );
//    load_belongs();
  };
  document.getElementById("study_form_list").innerHTML = text;
}
