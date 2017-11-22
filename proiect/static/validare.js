function validare() {
	var x = document.forms["form"]["FirstName"].value;
	var y = document.forms["form"]["LastName"].value;
	var z = document.forms["form"]["Mail"].value;
	var t = document.forms["form"]["pwd"].value;
	if (x == "" || y == "" || z == "" || t == "") {
		alert("Completati va rag campurile libere!");
		return false;


	} else {
		document.getElementById("form").submit();
	}
}
