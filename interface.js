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

function delete_course(uuid){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=delete_course&uuid="+uuid, false );
  jsonHttp.send( null );
  load_courses()
}

function data_load(){
  load_courses()
    load_materials()
}

function load_courses(){
  var jsonHttp = null;
  jsonHttp = new XMLHttpRequest();
  jsonHttp.open( "GET", "interface.py?query=courses", false );
  jsonHttp.send( null );
  var myobject = JSON.parse(jsonHttp.responseText);
  var text = "";
  for(i=0;i<myobject.courses.length;i++){
    text += "<div>"+ myobject.courses[i][1] + "<button onClick=\"delete_course(\'"+ myobject.courses[i][0] + "\')\">Удалить</button></div>";
  };
  document.getElementById("courses_list").innerHTML = text;
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
  document.getElementById("material_list_lists").innerHTML = text;
}
