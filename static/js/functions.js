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