var configMenu = document.querySelector(".post-config");

function abreConfig()
{
    configMenu.classList.toggle("post-config-height");
}

var escuro = document.getElementById("dark-btn");

escuro.onclick = function(){
    escuro.classList.toggle("dark-btn-on");
    document.body.classList.toggle("dark-theme");

    if(localStorage.getItem("theme") == "light"){
       localStorage.setItem("theme", "dark");
    }else{
        localStorage.setItem("theme", "light");
    }
}

if(localStorage.getItem("theme") == "light"){
    escuro.classList.remove("dark-btn-on");
    document.body.classList.remove("dark-theme");
}else if(localStorage.getItem("theme") == "dark"){
    escuro.classList.add("dark-btn-on");
    document.body.classList.add("dark-theme");
}else{
    localStorage.setItem("theme", "light");
    localStorage.setItem("theme");
}