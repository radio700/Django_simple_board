const mainicon = document.querySelector("#mi");


mainicon.width = 30;

function mouseov(){
  mainicon.width =35;
}

function outmouse(){
  mainicon.width =30;
}

// console.dir(mainicon);
mainicon.addEventListener("mouseover",mouseov)
mainicon.addEventListener("mouseout",outmouse)