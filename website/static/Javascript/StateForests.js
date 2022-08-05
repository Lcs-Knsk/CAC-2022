function unveilUploadForm(){
    var form = document.getElementById("uploadForm");
    if(form.style.display != "none"){
        form.style.display = "none";
    }
    else{
        form.style.display = "block";
    }
    console.log("Changed")
}

function sendToSignUp(){
   console.log("okay"); 
}