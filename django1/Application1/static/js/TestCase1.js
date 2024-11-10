let Defualt_or_Extended = false

function checkfield1()
    {
        alert("BUTTON IS CLICKED")

        if(document.getElementById("radio1").checked){
            Defualt_or_Extended = false
            alert("Zero")
        }else if(document.getElementById("radio2").checked){
            Defualt_or_Extended = true
            alert("One")
        }
    }