function validare() {
    var x = document.forms["form"]["FirstName"].value;
    var y = document.forms["form"]["LastName"].value;
    console.log(x);
    console.log(y);
    if (x == ""||y=="") {
        alert("Name must be filled out");
        return false;
    }
} 