$(function() {
  var url = window.location.href;
  $("ul.navbar-nav > li").removeClass("current")

  $(".navbar-collapse .nav-link").each(function() {
    if (url == (this.href)) {
      $(this).closest("li").addClass("current");
    }
  });
});


$(function() {
  var page = document.getElementsByTagName("title");
  if (page[0].innerHTML == " Iris B. Han ") {
    $("footer").css("display", "none");
    $("nav").css("background-color", "transparent");
  }
});


$(document).ready(function(){
  $(".card").hover(function(){
    var el = $(this).children().first()
    el.css("opacity", "0.4"); /*for mouseenter*/ 
    el.next().children().first().css("display", "block");
    }, function(){
    var el = $(this).children().first()
    el.css("opacity", "1"); /*for mouseleave*/
    el.next().children().first().css("display", "none");
  });
});


$(window).scroll(function() {
    var t = document.getElementById("returnTop");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    $(t).css("display", "block");
    } else {
    $(t).css("display", "none");
    }
});


function topFunction() {
  document.body.scrollTop = 0; //Safari
  document.documentElement.scrollTop = 0; //Chrome, Firefox, IE, Opera
}

