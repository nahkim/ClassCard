const basketStarterEL = document.querySelector("header .basket-starter");
const basketEL = basketStarterEL.querySelector(".basket");

basketStarterEL.addEventListener("click", function (event) {
  event.stopPropagation();
  if (basketEL.classList.contains("show")) {
    //hide
    // basketEL.classList.remove('show')
    hideBasket();
  } else {
    // basketEL.classList.add('show')
    showBasket();
  }
});
// 이벤트 전파가 되지않도록 만들기
basketEL.addEventListener("click", function (event) {
  event.stopPropagation();
});

window.addEventListener("click", function () {
  // basketEL.classList.remove('show')
  hideBasket();
});

// 복잡한 로직을 간단하게 함수로 "추상화" 했다
// 장바구니 보여주기
function showBasket() {
  basketEL.classList.add("show");
}
// 장바구니 사라지게 하기
function hideBasket() {
  basketEL.classList.remove("show");
}

// 검색!!!
const headerEl = document.querySelector("header");
// ... : 전개 연산자 spread operator
// 전개 연산자를 이용한 얕은 복사 shallow copy
const headerMenuEls = [...headerEl.querySelectorAll("ul.menu > li")];
const searchWrapEl = headerEl.querySelector(".search-wrap");
const searchStarterEl = headerEl.querySelector(".search-starter");
const searchCloserEl = searchWrapEl.querySelector(".search-closer");
const searchShadowEl = searchWrapEl.querySelector(".shadow");
const searchInputEl = searchWrapEl.querySelector("input");
const searchDelayEls = [...searchWrapEl.querySelectorAll("li")];

// searchStarterEl.addEventListener('click', function () {
//     showSearch()
// })

//  더 깔금하게 코드 작성하기
// 자바스크립트 part 에서 더 자세하게 공부필요!
searchStarterEl.addEventListener("click", showSearch);
searchCloserEl.addEventListener("click", hideSearch);
searchShadowEl.addEventListener("click", hideSearch);

function showSearch() {
  headerEl.classList.add("searching");
  document.documentElement.classList.add("fixed");
  // 순차적으로 사라지도록 만들었다.
  headerMenuEls.reverse().forEach(function (el, index) {
    //  index 숫자는 0 부터 시작한다.
    el.style.transitionDelay = (index * 0.4) / headerMenuEls.length + "s";
  });
  searchDelayEls.forEach(function (el, index) {
    el.style.transitionDelay = (index * 0.4) / searchDelayEls.length + "s";
  });
  setTimeout(function () {
    searchInputEl.focus();
  }, 600);
}
function hideSearch() {
  headerEl.classList.remove("searching");
  // 검색바가 나타나면 화면이 고정되도록 만들었다.
  document.documentElement.classList.remove("fixed");
  headerMenuEls.reverse().forEach(function (el, index) {
    el.style.transitionDelay = (index * 0.4) / headerMenuEls.length + "s";
  });
  searchDelayEls.reverse().forEach(function (el, index) {
    el.style.transitionDelay = (index * 0.4) / searchDelayEls.length + "s";
  });
  // 원래 상태로 다시 뒤집어 준다
  searchDelayEls.reverse();
  // 검색창 초기화
  searchInputEl.value = "";
}

gsap.from(".card", {
  duration: 3,
  opacity: 0,
  delay: 0.25,
  stagger: 0.6,
  ease: "elastic",
})(function ($) {
  "use strict";

  // Spinner
  var spinner = function () {
    setTimeout(function () {
      if ($("#spinner").length > 0) {
        $("#spinner").removeClass("show");
      }
    }, 1);
  };
  spinner();

  // Initiate the wowjs
  new WOW().init();

  // Sticky Navbar
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".sticky-top").addClass("shadow-sm").css("top", "0px");
    } else {
      $(".sticky-top").removeClass("shadow-sm").css("top", "-100px");
    }
  });

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".back-to-top").fadeIn("slow");
    } else {
      $(".back-to-top").fadeOut("slow");
    }
  });
  $(".back-to-top").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500, "easeInOutExpo");
    return false;
  });

  // Facts counter
  $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 2000,
  });

  // Testimonials carousel
  $(".testimonial-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    items: 1,
    dots: false,
    loop: true,
    nav: true,
    navText: [
      '<i class="bi bi-chevron-left"></i>',
      '<i class="bi bi-chevron-right"></i>',
    ],
  });
})(jQuery);

$(".tab-link").click(function () {
  var tab_id = $(this).attr("data-tab");

  $(".tab-link").removeClass("current");
  $(".tab-content").removeClass("current");

  $(this).addClass("current");
  $("#" + tab_id).addClass("current");
});




const badgeEl = document.querySelector('header .badges')
const toTopEl = document.querySelector('#to-top')
// 페이지에 스크롤 이벤트를 추가!
// 스크롤이 지나치게 자주 발생하는 것을 조절(throttle, 일부러 부하를 줌)
window.addEventListener('scroll', _.throttle(function () {
  // 페이지 스크롤 위치가 500px이 넘으면.
  if (window.scrollY > 500) {
    // Badge 요소 숨기기!
    gsap.to(badgeEl, .6, {
      opacity: 0,
      display: 'none'
    })
    // 상단으로 스크롤 버튼 보이기!
    gsap.to(toTopEl, .2, {
      x: 0
    })

  // 페이지 스크롤 위치가 500px이 넘지 않으면.
  } else {
    // Badge 요소 보이기!
    gsap.to(badgeEl, .6, {
      opacity: 1,
      display: 'block'
    })
    // 상단으로 스크롤 버튼 숨기기!
    gsap.to(toTopEl, .2, {
      x: 100
    })
  }
}, 300))
// 상단으로 스크롤 버튼을 클릭하면,
toTopEl.addEventListener('click', function () {
  // 페이지 위치를 최상단으로 부드럽게(0.7초 동안) 이동.
  gsap.to(window, .7, {
    scrollTo: 0
  })
})

