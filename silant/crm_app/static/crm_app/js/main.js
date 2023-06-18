$(function () {
  // --------------Сопровождение бургером скроллинга-----------------

  setInterval(() => {
    if (
      $(window).scrollTop() > 0 &&
      $(".header__top, .overlay").hasClass("header__top--open") === false
    ) {
      $(".burger").addClass("burger--follow");
    } else {
      $(".burger").removeClass("burger--follow");
    }
  }, 0);

  // ------------ Выкат/Закат Бургера и Overlay---------------------

  $(".burger, .overlay, .header__top a").on("click", function (e) {
    e.preventDefault();
    $(".header__top").toggleClass("header__top--open");
    $(".overlay").toggleClass("overlay--show");
  });
});
