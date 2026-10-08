<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prem Kumar Furniture | Luxury Interior Film</title>

<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%;overflow:hidden;background:#050505}
body{font-family:Arial,"Noto Sans Kannada",sans-serif;color:#fff}

#film{
  position:relative;width:100vw;height:100vh;
  overflow:hidden;background:#090909
}

.bg{
  position:absolute;inset:-4%;
  background:center/cover no-repeat;
  transition:background-image .8s ease;
  transform:scale(1);
  animation:cinema 8s linear forwards;
}
@keyframes cinema{
  from{transform:scale(1) translateX(0)}
  to{transform:scale(1.1) translateX(-1%)}
}

.dark{
  position:absolute;inset:0;
  background:
   linear-gradient(180deg,rgba(0,0,0,.15),rgba(0,0,0,.86)),
   radial-gradient(circle at 70% 40%,transparent,rgba(0,0,0,.65));
}

.top{
 position:absolute;z-index:8;top:24px;left:30px;right:30px;
 display:flex;justify-content:space-between;align-items:center
}
.logo{font-weight:900;letter-spacing:3px;font-size:18px}
.count{font-size:13px;opacity:.75}

.content{
 position:absolute;z-index:5;left:7%;bottom:9%;max-width:900px;
 animation:up .8s ease
}
@keyframes up{
 from{opacity:0;transform:translateY(35px)}
 to{opacity:1;transform:translateY(0)}
}

.tag{
 display:inline-block;padding:7px 13px;border:1px solid #fff5;
 border-radius:20px;background:#ffffff12;backdrop-filter:blur(10px);
 font-size:12px;letter-spacing:3px;margin-bottom:14px
}
h1{
 font-size:clamp(38px,7vw,82px);line-height:.95;
 font-weight:900;margin-bottom:18px
}
.dialogue{
 font-size:clamp(17px,2.3vw,27px);
 line-height:1.55;text-shadow:0 3px 12px #000
}

/* 3D STYLE PRODUCT CARD */
.card{
 position:absolute;z-index:4;right:8%;top:23%;
 width:245px;height:160px;perspective:900px
}
.card3{
 width:100%;height:100%;transform-style:preserve-3d;
 animation:spin 7s infinite linear
}
.face{
 position:absolute;inset:0;border:1px solid #fff3;
 border-radius:22px;background:#ffffff13;
 backdrop-filter:blur(14px);
 display:flex;align-items:center;justify-content:center;
 text-align:center;font-weight:800;letter-spacing:2px;
 box-shadow:0 20px 60px #0008
}
@keyframes spin{
 0%{transform:rotateY(0) rotateX(0)}
 50%{transform:rotateY(180deg) rotateX(5deg)}
 100%{transform:rotateY(360deg) rotateX(0)}
}

/* DATA */
.stats{margin-top:23px;max-width:520px}
.row{margin:10px 0}
.rowtop{display:flex;justify-content:space-between;font-size:12px}
.track{height:5px;background:#ffffff25;border-radius:10px;margin-top:5px}
.fill{
 height:100%;width:0;background:#fff;border-radius:10px;
 transition:width 1.3s ease
}

/* FLOATING 2D PARTICLES */
.particle{
 position:absolute;width:3px;height:3px;background:#fff;
 border-radius:50%;opacity:.3;animation:float 7s infinite linear
}
@keyframes float{
 from{transform:translateY(100vh) translateX(0)}
 to{transform:translateY(-10vh) translateX(80px)}
}

/* FINAL */
.final{
 position:absolute;z-index:20;inset:0;display:none;
 align-items:center;justify-content:center;text-align:center;
 background:radial-gradient(circle at center,#292929,#050505 70%);
 animation:fade 1s ease
}
.final.on{display:flex}
@keyframes fade{from{opacity:0}to{opacity:1}}

.final h2{
 font-size:clamp(38px,7vw,82px);letter-spacing:4px
}
.final p{font-size:20px;margin:16px 0}
.phone{font-size:clamp(23px,4vw,40px);font-weight:bold;line-height:1.7}
.badge{
 display:inline-block;margin-top:15px;padding:10px 18px;
 border:1px solid #fff4;border-radius:30px
}

/* CONTROLS */
.controls{
 position:absolute;z-index:30;bottom:22px;right:25px
}
button{
 border:0;border-radius:30px;padding:11px 17px;
 margin-left:5px;font-weight:bold;cursor:pointer
}
</style>
</head>

<body>

<div id="film">

<div class="bg" id="bg"></div>
<div class="dark"></div>

<div class="top">
 <div class="logo">PREM KUMAR FURNITURE</div>
 <div class="count" id="count">01 / 10</div>
</div>

<div class="content" id="content"></div>

<div class="card">
 <div class="card3">
  <div class="face">PREMIUM<br>INTERIORS</div>
 </div>
</div>

<div id="particles"></div>

<div class="final" id="final">
 <div>
  <h2>PREM KUMAR</h2>
  <p>Furniture • Interiors • Custom Work</p>
  <div class="phone">
   📞 9686470097<br>
   📞 9610631415
  </div>
  <p>Bengaluru • Karnataka</p>
  <div class="badge">YOUR DREAM HOME • OUR CRAFT</div>
 </div>
</div>

<div class="controls">
 <button onclick="music()">🎵 Music</button>
 <button onclick="restart()">↻ Replay</button>
</div>

<audio id="audio" loop>
 <source src="background-music.mp3" type="audio/mpeg">
</audio>

<script>

const scenes=[
["living-room.jpg","LIVING ROOM",
"ನಮ್ಮ ಮನೆಯ ಹೊಸ ಲುಕ್ ಬರೋಕೆ ಕಾರಣ ನಮ್ಮ ಫರ್ನಿಚರ್. ಪ್ರೇಮ್ ಕುಮಾರ್ ಫರ್ನಿಚರ್ ಮಾಡಿದ ಕೆಲಸ ನಿಜವಾಗಿಯೂ ತುಂಬಾ ಚೆನ್ನಾಗಿದೆ.",95,98],
["hall.jpg","LUXURY HALL",
"ನಮ್ಮ ಹಾಲ್‌ನ ಟಿವಿ ಯುನಿಟ್, ಕ್ಯಾಬಿನೆಟ್ ಮತ್ತು ವುಡ್ ವರ್ಕ್ ಎಲ್ಲವೂ ತುಂಬಾ ಪ್ರೀಮಿಯಂ ಆಗಿ ಕಾಣುತ್ತೆ.",96,97],
["kitchen.jpg","MODULAR KITCHEN",
"ಜಾಗವನ್ನು ಸರಿಯಾಗಿ ಯೂಸ್ ಮಾಡಿಕೊಂಡು ನಮ್ಮ ಕಿಚನ್‌ಗೆ ತುಂಬಾ ಚೆನ್ನಾದ ಸ್ಟೋರೇಜ್ ಕೊಟ್ಟಿದ್ದಾರೆ.",98,96],
["master.jpg","MASTER BEDROOM",
"ಬೆಡ್, ವಾರ್ಡ್ರೋಬ್ ಮತ್ತು ಡ್ರೆಸ್ಸಿಂಗ್ ಯುನಿಟ್ ಎಲ್ಲವನ್ನೂ ನಮ್ಮ ಅಗತ್ಯಕ್ಕೆ ತಕ್ಕಂತೆ ಕಸ್ಟಮೈಸ್ ಮಾಡಿದ್ದಾರೆ.",97,99],
["wardrobe.jpg","CUSTOM WARDROBE",
"ಪ್ರತಿಯೊಂದು ರೂಮ್‌ಗೂ ಜಾಗಕ್ಕೆ ಸರಿಯಾಗಿ ಫರ್ನಿಚರ್ ಮಾಡಿದ್ದಾರೆ. ಫಿನಿಷ್ ತುಂಬಾ ನೀಟ್ ಆಗಿದೆ.",99,98],
["kids.jpg","KIDS ROOM",
"ಮಕ್ಕಳ ರೂಮ್ ಕೂಡ ತುಂಬಾ ಚೆನ್ನಾಗಿ ಪ್ಲಾನ್ ಮಾಡಿದ್ದಾರೆ. ಸ್ಟೋರೇಜ್ ಮತ್ತು ಸ್ಟಡಿ ಸ್ಪೇಸ್ ಎರಡೂ ಇದೆ.",94,95],
["pooja.jpg","POOJA UNIT",
"ಮಾಡರ್ನ್ ಲುಕ್ ಜೊತೆಗೆ ನಮ್ಮ ಟ್ರಡಿಷನಲ್ ಟಚ್ ಕೂಡ ತುಂಬಾ ಸುಂದರವಾಗಿ ನೀಡಿದ್ದಾರೆ.",96,99],
["tv.jpg","TV & STORAGE",
"ಟಿವಿ ಯುನಿಟ್ ಮತ್ತು ಸ್ಟೋರೇಜ್ ಅನ್ನು ಮನೆಯ इंटीरियर ಜೊತೆ വളരെ ಚೆನ್ನಾಗಿ match ಮಾಡಿದ್ದಾರೆ.",98,97],
["dining.jpg","DINING AREA",
"ಡೈನಿಂಗ್ ಏರಿಯಾಗೂ ಸರಳವಾದ ಆದರೆ ತುಂಬಾ ಎಲಿಗಂಟ್ ಲುಕ್ ಕೊಟ್ಟಿದ್ದಾರೆ.",95,96],
["full-home.jpg","COMPLETE HOME",
"ನಿಮ್ಮ ಮನೆಗೂ ಬೆಸ್ಟ್ ಫರ್ನಿಚರ್ ಮತ್ತು ಇಂಟೀರಿಯರ್ ಬೇಕಾದ್ರೆ ಪ್ರೇಮ್ ಕುಮಾರ್ ಫರ್ನಿಚರ್ ಅವರನ್ನು ಸಂಪರ್ಕಿಸಿ.",99,99]
];

let i=0, timer;
const bg=document.getElementById("bg");
const content=document.getElementById("content");
const count=document.getElementById("count");
const final=document.getElementById("final");
const audio=document.getElementById("audio");

function render(){

 final.classList.remove("on");

 let s=scenes[i];

 bg.style.backgroundImage=`url("${s[0]}")`;

 content.innerHTML=`
  <div class="tag">${s[1]}</div>
  <h1>${s[1]}</h1>
  <div class="dialogue">${s[2]}</div>

  <div class="stats">

   <div class="row">
    <div class="rowtop">
     <span>Design Quality</span><span>${s[3]}%</span>
    </div>
    <div class="track">
     <div class="fill" style="width:${s[3]}%"></div>
    </div>
   </div>

   <div class="row">
    <div class="rowtop">
     <span>Finish & Detail</span><span>${s[4]}%</span>
    </div>
    <div class="track">
     <div class="fill" style="width:${s[4]}%"></div>
    </div>
   </div>

  </div>
 `;

 count.innerText=
  String(i+1).padStart(2,"0")+" / "+
  String(scenes.length).padStart(2,"0");

 bg.style.animation="none";
 void bg.offsetWidth;
 bg.style.animation="cinema 8s linear forwards";
}

function next(){
 i++;

 if(i>=scenes.length){
   final.classList.add("on");
   i=0;

   setTimeout(()=>{
     final.classList.remove("on");
     render();
   },5000);

   return;
 }
 render();
}

function restart(){
 clearInterval(timer);
 i=0;
 final.classList.remove("on");
 render();
 timer=setInterval(next,7000);
}

function music(){
 if(audio.paused) audio.play();
 else audio.pause();
}

/* PARTICLES */
for(let n=0;n<35;n++){
 let p=document.createElement("div");
 p.className="particle";
 p.style.left=Math.random()*100+"%";
 p.style.animationDelay=Math.random()*7+"s";
 p.style.animationDuration=(5+Math.random()*6)+"s";
 document.getElementById("particles").appendChild(p);
}

render();
timer=setInterval(next,7000);

</script>

</div>
</body>
</html>
