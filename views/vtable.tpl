<div class="list_element">
<table>
<tr>
%for j in range(0,len(headers)):
	<td class=field_name>{{!headers[j]}}</td>
%end
%if defined('editable'):
<td></td>
%end
</tr>
%for i in data:
	<tr>
	%uuid = i[0]
	%for j in range(0,len(headers)):
		<td class=field_value>
		{{!i[j+1]}}
		</td>
	%end
	<td>
	%if defined('editable'):
	%include edit_delete_btns uuid = uuid, action = action, editdelete = editable
	%end
	</td>
	</tr>
%end
</table>
</div>
