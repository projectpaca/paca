var linkDiv = document.getElementById("navID");
var links = linkDiv.getElementsByClassName("link");

for (var i = 0;i < links.length;i++) {
    links[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}


/*
function changeColor() {
    var links = linkContainer.getElementsByClassName("link");
    for (var i=0; i < document.links.length; i++) {
        links[i].onclick(){
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace("link","active");
            this.className += "active";
        }
    }
    
}

changeColor()
*/