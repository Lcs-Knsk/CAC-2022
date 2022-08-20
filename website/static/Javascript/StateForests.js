function unveilUploadForm(){
    var form = document.getElementById("uploadForm");

    if(form.style.display != "block"){
        form.style.display = "block";
    }
    else{
        form.style.display = "none";
    }
    console.log("Changed");
}

function sendToSignUp(){
   console.log("okay"); 
}