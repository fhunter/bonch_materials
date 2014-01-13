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

function add_course(){
  var jsonHttp = null;
  var name = document.getElementById("course_name").value;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=add_course&name="+name, false );
  jsonHttp.send( null );
  load_courses()
}

function add_material(){
}

function add_author(){
}

function add_speciality(){
}

function add_discipline(){
}

function add_study_form(){
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
    text += "<div>"+ myobject.materials[i][0] + " - "+ myobject.materials[i][1] + "</div>";
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
    text += "<div class=\"list_element\">"+ myobject.authors[i][1] + "<button onClick=\"javascript:delete_author('" + myobject.authors[i][0] + "')\">Удалить</button></div>";
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
    text += "<div class=\"list_element\">"+ myobject.speciality[i][1] +" = "+ myobject.speciality[i][2] + "<button onClick=\"javascript:delete_speciality('" + myobject.speciality[i][0] + "')\">Удалить</button></div>";
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
    text += "<div class=\"list_element\">"+ myobject.discipline[i][1] +" = "+ myobject.discipline[i][2] + "<button onClick=\"javascript:delete_discipline('" + myobject.discipline[i][0] + "')\">Удалить</button></div>";
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
    text += "<div class=\"list_element\">"+ myobject.study_form[i][1] + "<button onClick=\"javascript:delete_study_form('" + myobject.study_form[i][0] + "')\">Удалить</button></div>";
//    load_belongs();
  };
  document.getElementById("study_form_list").innerHTML = text;
}
