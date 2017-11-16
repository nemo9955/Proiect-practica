function validare() {
    var x = document.forms["form"]["FirstName"].value;
    var y = document.forms["form"]["Lastname"].value;
    if (x == ""||y=="") {
        alert("Name must be filled out");
        return false;
    }
} 