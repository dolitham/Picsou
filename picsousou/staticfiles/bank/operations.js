var checkboxes = document.querySelectorAll("input[name=operation_check]");

function display(t) {
  var t2 = document.getElementById("t2");
  t2.firstChild.nodeValue = t;
}

checkboxes.forEach(function(checkbox){
    checkbox.addEventListener('click', function() {
        operation_id = this.id.toString()
        if (this.checked) {
            display("checking operation id="+operation_id);
            var url = new URL('http://127.0.0.1:8000/bank/check_operation_id/')
        }
        else {
            display("unchecking operation id="+operation_id);
            var url = new URL('http://127.0.0.1:8000/bank/uncheck_operation_id/')
        }
        var params = [['operation_id', operation_id]]
        url.search = new URLSearchParams(params)
        fetch(url)
    }, false);
});
