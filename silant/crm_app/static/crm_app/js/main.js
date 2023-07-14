$(function () {
  // --------------Сопровождение бургером скроллинга-----------------

  setInterval(() => {
    if (
      $(window).scrollTop() > 0 &&
      $(".header__top").hasClass("header__top--open") === false
    ) {
      $(".burger").addClass("burger--follow");
    } else {
      $(".burger").removeClass("burger--follow");
    }
  }, 0);

  // ------------ Выкат/Закат Бургера и Overlay---------------------

  $(".burger, .overlay").on("click", function (e) {
    e.preventDefault();
    $(".header__top").toggleClass("header__top--open");
    $(".overlay").toggleClass("overlay--show");
  });
});

// ------------ Аккордеон в СПРАВОЧНИКАХ ---------------------

$(".refbook__acc-link").on("click", function (e) {
  e.preventDefault();
  if ($(this).hasClass("refbook__acc-link--active")) {
    $(this).removeClass("refbook__acc-link--active");
    $(this).children(".refbook__acc-text").slideUp();
  } else {
    $(".refbook__acc-link").removeClass("refbook__acc-link--active");
    $(".refbook__acc-text").slideUp();
    $(this).addClass("refbook__acc-link--active");
    $(this).children(".refbook__acc-text").slideDown();
  }
});
