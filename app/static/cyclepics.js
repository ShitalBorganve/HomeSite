NewImg = new Array (
"Donquixote.jpg",
"Starrynight.jpg",
"Monalisa.jpg"
);

var ImgNum = 0;
var ImgLength = NewImg.length - 1;
var delay = 5000;
var lock = false;
var run;

function chgImg(direction) {
  if (document.images) {
    ImgNum = ImgNum + direction;
    if (ImgNum > ImgLength) { ImgNum = 0; }
    if (ImgNum < 0) { ImgNum = ImgLength; }
    document.getElementByID('slideshow'.src = NewImg[ImgNum];
  }
}

function auto() {
  if (lock == true) {
    lock = false;
    window.clearInterval(run);
  }
  else if (lock == false) {
    lock = true;
    run = setInterval("chImg(1)", delay);
  }
}
