const darklight = document.getElementById("dark-switch");
const body = document.getElementById("body");
const nav_dark = document.getElementById("nav");
const doc_dark = document.getElementById("doc-bar");
const searchterm = document.getElementById("query");
const searchbtn = document.getElementById("query-btn");
const login_menu = document.getElementById("login-sub-menu");
const addlist_menu = document.getElementById("add-list-sub-menu");
const ele_tito = document.getElementById("contain-seco");
const ele_tit = document.getElementById("contain-sec");
const ele_tit2 = document.getElementById("contain-sec2");
const ele_tit3 = document.getElementById("contain-sec3");
const ele_tit4 = document.getElementById("contain-sec4");
const ele_tit5 = document.getElementById("contain-sec5");
const ele_tit6 = document.getElementById("contain-sec6");
const ele_tit7 = document.getElementById("contain-sec7");
const ele_tit8 = document.getElementById("contain-sec8");
const ele_tit9 = document.getElementById("contain-sec9");
const ele_tit10 = document.getElementById("contain-sec10");
const head_topo = document.getElementById("headlline-topo");
const head_top = document.getElementById("headlline-top");
const head_middle = document.getElementById("headline-middle");
const head_bottom = document.getElementById("headline-bottom");
const fout = document.getElementById("fout");
const poster = document.getElementById("poster");
const about_us_body = document.getElementById("about_us_body");
const main_op = document.getElementById("main-opp");
const gen_op = document.getElementById("gen-op");
const list_form = document.getElementById("listfor");
const list_detail = document.getElementById("list-det-id");
const movie_menu = document.getElementById("movie-disp");
const music_menu = document.getElementById("music-disp");
const book_menu = document.getElementById("book-disp");
const comments = document.getElementById("comments-id");
const posteditcomments = document.getElementById("title-comment");

function save() {	
    var checkbox = document.getElementById("dark-switch");
    localStorage.setItem("dark-switch", checkbox.checked);	
}

//for loading
var checked = JSON.parse(localStorage.getItem("dark-switch"));
    document.getElementById("dark-switch").checked = checked;


function darkmode(checkbox) {
    if(checkbox.checked == true){
        body?.classList.toggle("body-dark-mode");
        nav_dark?.classList.toggle("nav-dark-mode");
        doc_dark?.classList.toggle("doc-bar-dark-mode");
        searchterm?.classList.toggle("searchTerm-dark-mode");
        searchbtn?.classList.toggle("searchButton-dark-mode");
        login_menu?.classList.toggle("login-sub-menu-dark-mode");
        addlist_menu?.classList.toggle("add-list-sub-menu-dark-mode");
        head_topo?.classList.toggle("headline-topo-dark-mode");
        head_top?.classList.toggle("headline-top-dark-mode");
        head_middle?.classList.toggle("headline-middle-dark-mode");
        head_bottom?.classList.toggle("headline-bottom-dark-mode");
        fout?.classList.toggle("fout-dark-mode");
        ele_tito?.classList.toggle("contain-sec-dark-mode");
        ele_tit?.classList.toggle("contain-sec-dark-mode");
        ele_tit2?.classList.toggle("contain-sec-dark-mode");
        ele_tit3?.classList.toggle("contain-sec-dark-mode");
        ele_tit4?.classList.toggle("contain-sec-dark-mode");
        ele_tit5?.classList.toggle("contain-sec-dark-mode");
        ele_tit6?.classList.toggle("contain-sec-dark-mode");
        ele_tit7?.classList.toggle("contain-sec-dark-mode");
        ele_tit8?.classList.toggle("contain-sec-dark-mode");
        ele_tit9?.classList.toggle("contain-sec-dark-mode");
        ele_tit10?.classList.toggle("contain-sec-dark-mode");
        about_us_body?.classList.toggle("about_us_h1_dark_mode");
        main_op?.classList.toggle("main-op-dark-mode");
        gen_op?.classList.toggle("title-dark-mode");
        list_form?.classList.toggle("listform-dark-mode");
        list_detail?.classList.toggle("list_detail_dark_mode");
        movie_menu?.classList.toggle("nav-menu-dark-mode");
        music_menu?.classList.toggle("nav-menu-dark-mode");
        book_menu?.classList.toggle("nav-menu-dark-mode");
        comments?.classList.toggle("commentss-dark-mode");
        posteditcomments?.classList.toggle("title-com-dark-mode");
    }
    else{
        body?.classList.remove("body-dark-mode");
        nav_dark?.classList.remove("nav-dark-mode");
        doc_dark?.classList.remove("doc-bar-dark-mode");
        searchterm?.classList.remove("searchTerm-dark-mode");
        searchbtn?.classList.remove("searchButton-dark-mode");
        login_menu?.classList.remove("login-sub-menu-dark-mode");
        addlist_menu?.classList.remove("add-list-sub-menu-dark-mode");
        head_topo?.classList.remove("headline-topo-dark-mode");
        head_top?.classList.remove("headline-top-dark-mode");
        head_middle?.classList.remove("headline-middle-dark-mode");
        head_bottom?.classList.remove("headline-bottom-dark-mode");
        fout?.classList.remove("fout-dark-mode");
        ele_tito?.classList.remove("contain-sec-dark-mode");
        ele_tit?.classList.remove("contain-sec-dark-mode");
        ele_tit2?.classList.remove("contain-sec-dark-mode");
        ele_tit3?.classList.remove("contain-sec-dark-mode");
        ele_tit4?.classList.remove("contain-sec-dark-mode");
        ele_tit5?.classList.remove("contain-sec-dark-mode");
        ele_tit6?.classList.remove("contain-sec-dark-mode");
        ele_tit7?.classList.remove("contain-sec-dark-mode");
        ele_tit8?.classList.remove("contain-sec-dark-mode");
        ele_tit9?.classList.remove("contain-sec-dark-mode");
        ele_tit10?.classList.remove("contain-sec-dark-mode");
        about_us_body?.classList.remove("about_us_h1_dark_mode");
        main_op?.classList.remove("main-op-dark-mode");
        gen_op?.classList.remove("title-dark-mode");
        list_form?.classList.remove("listform-dark-mode");
        list_detail?.classList.remove("list_detail_dark_mode");
        movie_menu?.classList.remove("nav-menu-dark-mode");
        music_menu?.classList.remove("nav-menu-dark-mode");
        book_menu?.classList.remove("nav-menu-dark-mode");
        comments?.classList.remove("commentss-dark-mode");
        posteditcomments?.classList.remove("title-com-dark-mode");
    }
}
darkmode(document.getElementById("dark-switch"));




