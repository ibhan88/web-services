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
  if (page[0].innerHTML == " Home ") {
    $("footer").css("display", "none");
  }
});


$(document).ready(function(){
  $(".card").hover(function(){
    var el = $(this).children().first()
    el.css("opacity", "0.4"); /*for mouseenter*/ 
    el.next().css("display", "block");
    }, function(){
    var el = $(this).children().first()
    el.css("opacity", "1"); /*for mouseleave*/
    el.next().css("display", "none");
  });
});