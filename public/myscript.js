function changeToExps() {
    let aboutDiv = document.querySelector("#about");
    let aboutSpan = document.querySelector("#spanabout");
    let expsDiv = document.querySelector("#exps");
    let expsSpan = document.querySelector("#spanexps");
    aboutDiv.style.display = "none";
    expsDiv.style.display = "block";
    aboutSpan.style.backgroundColor="#333";
    expsSpan.style.backgroundColor="#467500";
    aboutSpan.style.fontSize = "20px";
    expsSpan.style.fontSize = "25px";
}
function changeToAbout() {
    let aboutDiv = document.querySelector("#about");
    let aboutSpan = document.querySelector("#spanabout");
    let expsDiv = document.querySelector("#exps");
    let expsSpan = document.querySelector("#spanexps");
    aboutDiv.style.display = "block";
    expsDiv.style.display = "none";
    aboutSpan.style.backgroundColor="#467500";
    expsSpan.style.backgroundColor="#333";
    aboutSpan.style.fontSize = "25px";
    expsSpan.style.fontSize = "20px";
}
function out(){
  let aboutSpan = document.querySelector("#spanabout");
  let expsSpan = document.querySelector("#spanexps");
  aboutSpan.style.backgroundColor="#333";
  expsSpan.style.backgroundColor="#333";
  aboutSpan.style.fontSize = "20px";
  expsSpan.style.fontSize = "20px";
}