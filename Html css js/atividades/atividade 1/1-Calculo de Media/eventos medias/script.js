const display = document.getElementById("display");
const clear = document.getElementById("clear");
const back = document.getElementById("backspace");
const total = document.getElementById("total");

clear.addEventListener("click",()=>{
    display.value = "";
})

back.addEventListener("click",()=>{
    display.value = display.value.slice(0,-1);
});

total.addEventListener("click",()=>{
    display.value = eval(display.value);
});



buttons = [...document.getElementsByTagName("button")];


for(let i = 2;i < buttons.length-1;i++){
    buttons[i].addEventListener("click", function() {
        display.value += this.textContent;
    });
}