const bigbull = document.getElementById("bigbull")
const bulgogi = document.getElementById("bulgogi")
const hotcrispy = document.getElementById("hotcrispy")

const total_num = document.querySelector("p.total_num")
const menu_show = document.querySelector("p.menu_show")

function onclicksubmit1(){
  menu_show.innerText = String("bigbull");
  total_num.innerText = parseInt(total_num.innerText)+1;
  
}
function onclicksubmit2(){
  console.log("bulgogi");
}
function onclicksubmit3(){
  console.log("hotcrispy");
}


bigbull.addEventListener("click",onclicksubmit1)
bulgogi.addEventListener("click",onclicksubmit2)
hotcrispy.addEventListener("click",onclicksubmit3)


