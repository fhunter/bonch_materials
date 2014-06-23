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

function gen_table_row(name, value ){
    var text = "";
    text += "<tr>";
    text += "<td class=field_name>" + name + "</td>";
    text += "<td class=field_value>" + value + "</td>";
    text += "</tr>";
    return text;
}

function gen_table_row_wide( name, value ){ 
    var text = "";
    text += "<tr><td class=field_name>" + name + "</td></tr>";
    text += "<tr><td class=field_value colspan=2>" + value + "</td></tr>";
    return text;
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

function load_authors(){
  var myobject = fetch_json("query=authors");
  var text = "";
  for(i=0;i<myobject.authors.length;i++){
    text += "<div class=\"list_element\">";
    text += "<table>";
    text += gen_table_row( "ФИО автора", myobject.authors[i][1] );
    text += "</table>";
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
    text += "<table>";
    text += gen_table_row( "Шифр", myobject.speciality[i][1] );
    text += gen_table_row( "Название", myobject.speciality[i][2] );
    text += gen_table_row_wide( "Описание", myobject.speciality[i][3] );
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
    text += "<table>";
    text += gen_table_row( "Название", myobject.discipline[i][1] );
    text += gen_table_row( "Семестр", myobject.discipline[i][2] );
    text += gen_table_row_wide( "Описание", myobject.discipline[i][3] );
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
    text += "<table>";
    text += gen_table_row( "Форма обучения", myobject.study_form[i][1] );
    text += "</table>";
    text += insert_delete_btn( myobject.study_form[i][0], "delete_study_form" );
//    load_belongs();
  };
  document.getElementById("study_form_list").innerHTML = text;
}
