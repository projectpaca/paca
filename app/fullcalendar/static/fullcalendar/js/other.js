var linkDiv = document.getElementById("navID"),
    links = linkDiv.getElementsByClassName("link");
// navID är id på diven som håller länkarna
// link är en klass, som varje länk har i sin a-tag

for (i = 0; i < links.length; i++) {
    links[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}
// när användaren klickar på en länk så ändras statusen på den länken
// till "active". Endast en länk i taget kan vara aktiv.  