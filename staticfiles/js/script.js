const menuBtn = document.querySelector('.menu-btn');
const subMenu = document.querySelector('.submenu');
const movieMore = document.querySelector('.movie-more');
const movieExpand = document.querySelector('.movie-expand');
const bookMore = document.querySelector('.book-more');
const bookExpand = document.querySelector('.book-expand');
const musicMore = document.querySelector('.music-more');
const musicExpand = document.querySelector('.music-expand');
const navmovieMore = document.querySelector('#movie-disp');
const navmovieExpand = document.querySelector('.nav-movie-expand');
const navbookMore = document.querySelector('#book-disp');
const navbookExpand = document.querySelector('.nav-book-expand');
const navmusicMore = document.querySelector('#music-disp');
const navmusicExpand = document.querySelector('.nav-music-expand');
const userdoclogo = document.querySelector('.user-doc-logo');
const userdocmenu = document.querySelector('.login-sub-menu');
const addlist = document.querySelector('#add-list-butt');
const addlistmenu = document.querySelector('.add-list-sub-menu');
const loader = document.getElementById("preloader");
const comment_rate = document.getElementById("id_rate");
const st1 = document.getElementById("st1");
const st2 = document.getElementById("st2");
const st3 = document.getElementById("st3");
const st4 = document.getElementById("st4");
const st5 = document.getElementById("st5");




// star hover
// if(st1){
//   st1.addEventListener('mouseover', () => {
    
//     st1.className = "fa fa-star checked";
//     st2.className = "fa fa-star";
//     st3.className = "fa fa-star";
//     st4.className = "fa fa-star";
//     st5.className = "fa fa-star";
//   });
//   }
//   if(st2){
//   st2.addEventListener('mouseover', () => {
//     st1.className = "fa fa-star checked";
//     st2.className = "fa fa-star checked";
//     st3.className = "fa fa-star";
//     st4.className = "fa fa-star";
//     st5.className = "fa fa-star";
//   });
//   }
//   if(st3){
//   st3.addEventListener('mouseover', () => {
//     st1.className = "fa fa-star checked";
//     st2.className = "fa fa-star checked";
//     st3.className = "fa fa-star checked";
//     st4.className = "fa fa-star";
//     st5.className = "fa fa-star";
//   });
//   }
//   if(st4){
//   st4.addEventListener('mouseover', () => {
//     st1.className = "fa fa-star checked";
//     st2.className = "fa fa-star checked";
//     st3.className = "fa fa-star checked";
//     st4.className = "fa fa-star checked";
//     st5.className = "fa fa-star";
//   });
//   }
//   if(st5){
//   st5.addEventListener('mouseover', () => {
//     st1.className = "fa fa-star checked";
//     st2.className = "fa fa-star checked";
//     st3.className = "fa fa-star checked";
//     st4.className = "fa fa-star checked";
//     st5.className = "fa fa-star checked";
//   });
//   }


// star clicked
if(st1){
st1.addEventListener('click', () => {
  
  st1.className = "fa fa-star checked";
  st2.className = "fa fa-star";
  st3.className = "fa fa-star";
  st4.className = "fa fa-star";
  st5.className = "fa fa-star";
  comment_rate.value = "1";
});
}
if(st2){
st2.addEventListener('click', () => {
  st1.className = "fa fa-star checked";
  st2.className = "fa fa-star checked";
  st3.className = "fa fa-star";
  st4.className = "fa fa-star";
  st5.className = "fa fa-star";
  comment_rate.value = "2";
});
}
if(st3){
st3.addEventListener('click', () => {
  st1.className = "fa fa-star checked";
  st2.className = "fa fa-star checked";
  st3.className = "fa fa-star checked";
  st4.className = "fa fa-star";
  st5.className = "fa fa-star";
  comment_rate.value = "3";
});
}
if(st4){
st4.addEventListener('click', () => {
  st1.className = "fa fa-star checked";
  st2.className = "fa fa-star checked";
  st3.className = "fa fa-star checked";
  st4.className = "fa fa-star checked";
  st5.className = "fa fa-star";
  comment_rate.value = "4";
});
}
if(st5){
st5.addEventListener('click', () => {
  st1.className = "fa fa-star checked";
  st2.className = "fa fa-star checked";
  st3.className = "fa fa-star checked";
  st4.className = "fa fa-star checked";
  st5.className = "fa fa-star checked";
  comment_rate.value = "5";
});
}
// window.addEventListener("load", function(){
//   loader.style.display = "none";
// })
// .value = "My value";



let addlistclick = false;
addlist.addEventListener('click', () => {
  if(!addlistclick) {
    addlistmenu.style.left = "0px";
    addlistclick = true;
    addlistmenu.style.transition = "all 250ms ease-in-out";
    userdocmenu.style.left = "-200px";
  } else {
    addlistmenu.style.left = "-65px";
    addlistclick = false;
  }
});


let menuOpen = false;
let movieExpandOpen = false;
let bookExpandOpen = false;
let musicExpandOpen = false;
let navmovieExpandOpen = false;
let navmusicExpandOpen = false;
let navbookExpandOpen = false;
let userdoclogoOpen = false;

userdoclogo.addEventListener('click', () => {
  if(!userdoclogoOpen){
    userdocmenu.style.bottom = "42px";
    userdocmenu.style.left = "5px";
    userdoclogoOpen = true;
    userdocmenu.style.transition = "all 100ms ease-in-out";
    addlistmenu.style.left = "-65px";

  } else {
    userdocmenu.style.left = "-200px";
    userdoclogoOpen = false;
  }
});

menuBtn.addEventListener('click', () => {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    subMenu.style.bottom = "76px";
    subMenu.style.transition = "all 250ms ease-in-out";
    document.body.scrollTop = 0;
    // document.documentElement.scrollTop = 0;
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    subMenu.style.bottom = "-200px";
    movieMore.style.display = "none";
    musicMore.style.display = "none";
    bookMore.style.display = "none";
    subMenu.style.transition = "all 250ms ease-in-out";
  }
});
movieExpand.addEventListener('click', () =>{
  if(!movieExpandOpen){
    movieMore.style.display = "block";
    musicMore.style.display = "none";
    bookMore.style.display = "none";
    movieExpandOpen = true;
    movieMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    movieMore.style.display = "none";
    movieExpandOpen = false;
    movieMore.style.transition = "all 250ms ease-in-out";
  }
});
bookExpand.addEventListener('click', () =>{
  if(!bookExpandOpen){
    bookMore.style.display = "block";
    movieMore.style.display = "none";
    musicMore.style.display = "none";
    bookExpandOpen = true;
    bookMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    bookMore.style.display = "none";
    bookExpandOpen = false;
    bookMore.style.transition = "all 250ms ease-in-out";
  }
});
musicExpand.addEventListener('click', () =>{
  if(!musicExpandOpen){
    musicMore.style.display = "block";
    movieMore.style.display = "none";
    bookMore.style.display = "none";
    musicExpandOpen = true;
    musicMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    musicMore.style.display = "none";
    musicExpandOpen = false;
    musicMore.style.transition = "all 250ms ease-in-out";
  }
});



// desktop menu functions

navmovieExpand.addEventListener('click', () =>{
  if(!navmovieExpandOpen){
    navmovieMore.style.display = "flex";
    navmusicMore.style.display = "none";
    navbookMore.style.display = "none";
    navmovieExpandOpen = true;
    navmovieMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    navmovieMore.style.display = "none";
    navmovieExpandOpen = false;
    navmovieMore.style.transition = "all 250ms ease-in-out";
  }
});
navbookExpand.addEventListener('click', () =>{
  if(!navbookExpandOpen){
    navbookMore.style.display = "flex";
    navmovieMore.style.display = "none";
    navmusicMore.style.display = "none";
    navbookExpandOpen = true;
    navbookMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    navbookMore.style.display = "none";
    navbookExpandOpen = false;
    navbookMore.style.transition = "all 250ms ease-in-out";
  }
});
navmusicExpand.addEventListener('click', () =>{
  if(!navmusicExpandOpen){
    navmusicMore.style.display = "flex";
    navbookMore.style.display = "none";
    navmovieMore.style.display = "none";
    navmusicExpandOpen = true;
    navmusicMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    navmusicMore.style.display = "none";
    navmusicExpandOpen = false;
    navmusicMore.style.transition = "all 250ms ease-in-out";
  }
});

const related_btn = document.getElementById("related-arrow-btn");
const related_close = document.getElementById("related-close-btn");
const related_slide_menu = document.getElementById("related-slide-menu");

related_btn?.addEventListener('click',() => {
  related_slide_menu.style.right = "0px";
  related_btn.style.display = "none";
  related_btn.style.transition = "all 300ms ease-in-out";
  related_slide_menu.style.transition = "all 300ms ease-in-out";
});

related_close?.addEventListener('click',() => {
  related_slide_menu.style.right = "-300px";
  related_btn.style.display = "flex";
})



