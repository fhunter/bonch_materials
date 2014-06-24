
function fetch_json(request){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?" + request, false );
  jsonHttp.send( null );
  return JSON.parse(jsonHttp.responseText);
}

function add_material(){
  load_materials()
}

function add_author(){
  var name = document.getElementById("authors_name").value;
  fetch_json( "query=add_author&fio="+name);
  load_authors()
}

function add_speciality(){
  var name = document.getElementById("speciality_name").value;
  var code = document.getElementById("speciality_code").value;
  var desc = document.getElementById("speciality_description").value;
  fetch_json( "query=add_speciality&name="+name+"&code="+code+"&desc="+desc );
  load_specialities()
}

function add_discipline(){
  var name = document.getElementById("discipline_name").value;
  var sem = document.getElementById("discipline_semester").value;
  var desc = document.getElementById("discipline_description").value;
  fetch_json( "query=add_discipline&name="+name+"&sem="+sem+"&desc="+desc);
  load_disciplines()
}

function add_study_form(){
  var name = document.getElementById("study_form_name").value;
  fetch_json( "query=add_study_form&name="+name);
  load_study_forms()
}

function delete_material(uuid){
  fetch_json( "query=delete_material&uuid="+uuid );
  load_materials()
}

function delete_author(uuid){
  fetch_json( "query=delete_author&uuid="+uuid );
  load_authors()
}

function delete_speciality(uuid){
  fetch_json( "query=delete_speciality&uuid="+uuid );
  load_specialities()
}

function delete_discipline(uuid){
  fetch_json( "query=delete_discipline&uuid="+uuid );
  load_disciplines()
}

function delete_study_form(uuid){
  fetch_json( "query=delete_study_form&uuid="+uuid );
  load_study_forms()
}

