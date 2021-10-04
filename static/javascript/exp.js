const mainicon = document.querySelector("#mi");


console.dir(mainicon);
mainicon.width = 30;

function mouseov(){
  mainicon.width =35;
}

function outmouse(){
  mainicon.width =30;
}

mainicon.addEventListener("mouseover",mouseov)
mainicon.addEventListener("mouseout",outmouse)