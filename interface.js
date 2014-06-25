
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

function add_discipline(){
  var name = document.getElementById("discipline_name").value;
  var sem = document.getElementById("discipline_semester").value;
  var desc = document.getElementById("discipline_description").value;
  fetch_json( "query=add_discipline&name="+name+"&sem="+sem+"&desc="+desc);
  load_disciplines()
}

function delete_material(uuid){
  fetch_json( "query=delete_material&uuid="+uuid );
  load_materials()
}

function delete_author(uuid){
  fetch_json( "query=delete_author&uuid="+uuid );
  load_authors()
}

function delete_discipline(uuid){
  fetch_json( "query=delete_discipline&uuid="+uuid );
  load_disciplines()
}
