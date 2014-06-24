
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

function data_load(){
  load_materials()
  load_authors()
  load_specialities()
  load_disciplines()
  load_study_forms()
}

function load_belongs(uuid){
  var myobject = fetch_json("query=author_for_material&uuid="+uuid);
  return myobject;
}

function load_materials(){
  var myobject = fetch_json("query=materials");
  var text = "";
  for(i=0;i<myobject.materials.length;i++){
    text += "<div class=\"list_element\">";
    text += "<table>";
    text += gen_table_row( "Название" , myobject.materials[i][1]);
    text += gen_table_row( "Дата заливки" , myobject.materials[i][4]);
    if(myobject.materials[i][5]==null){
      myobject.materials[i][5]="Никогда";
    }
    text += gen_table_row( "Дата редактирования" , myobject.materials[i][5]);
    text += gen_table_row( "Заливал", myobject.materials[i][3]);
    tmp = load_belongs(myobject.materials[i][0]);
    for(j = 0; j<tmp.belongs.length;j++){
      text += gen_table_row( "Автор", tmp.belongs[j][1]);
     //  + "-" + tmp.belongs[j][0]); Добавить кнопку для удаления автора по uuid-у
    };
    text += gen_table_row_wide( "Описание", myobject.materials[i][2]);
    text += "</table>";
    text += insert_delete_btn(myobject.materials[i][0], "delete_material");
//    load_belongs();
  };
  document.getElementById("material_list").innerHTML = text;
}

