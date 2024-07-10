
// alert("Hello, Harsha!!!")

const user_text = document.querySelector('.text_box')
const send = document.querySelector('.sub_btn')
const user = document.querySelector('.user h3')
const genai = document.querySelector('.genai h3')
var loader = document.getElementById("preloader");
const c_d = document.querySelector('.content div')
const speak_btn = document.querySelector('.speak-btn')

if (user.textContent == ''){
    user.style.visibility = 'hidden';
}else{
    user.style.visibility = 'visible';
    
}
if (genai.textContent == ''){
    genai.style.visibility = 'hidden';
    speak_btn.style.visibility = 'hidden';

}else{
    genai.style.visibility = 'visible';
    speak_btn.style.visibility = 'visible';

}


send.addEventListener('click', ()=>{
    user.textContent = user_text.value;
    user.style.visibility = 'visible';
    genai.textContent = '...';
    genai.style.visibility = 'visible';
})

// window.addEventListener("load", ()=>{
//     loader.style.display = "none";
// })


