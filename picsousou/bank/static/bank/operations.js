var checkbox = document.querySelectorAll("input[name=operation_check]");

function modifyText(t) {
  var t2 = document.getElementById("t2");
  t2.firstChild.nodeValue = t;
}

checkbox.forEach(function(c){
    c.addEventListener('click', function() {
        if(this.checked) {
                modifyText("checked");
        } else {
                modifyText("unchecked");
        }
    }, false);
});
