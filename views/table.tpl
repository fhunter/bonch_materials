%for i in data:
	<div class="list_element">
	<table>
	%uuid = i[0]
	%for j in range(0,len(headers)):
		<tr><td class=field_name>{{headers[j]}}</td>
		%if(width[j]):
			</tr><tr><td class=field_value colspan=2>
		%else:
			<td class=field_value>
		%end
		{{i[j+1]}}</td>
		</tr>
	%end
	</table>
	%if defined('editable'):
	%include edit_delete_btns uuid = uuid, action = action
	%end
	</div>
%end
