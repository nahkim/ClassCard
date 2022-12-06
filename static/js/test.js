const basketStarterEL = document.querySelector('header .basket-starter')
const basketEL = basketStarterEL.querySelector('.basket')

basketStarterEL.addEventListener('click', function(event){
    event.stopPropagation()
    if (basketEL.classList.contains('show')) {
        //hide
        // basketEL.classList.remove('show')
        hideBasket()
    }else{
        // basketEL.classList.add('show')
        showBasket()
    }
})
// 이벤트 전파가 되지않도록 만들기
basketEL.addEventListener('click', function (event) {
    event.stopPropagation()
})


window.addEventListener('click', function() {
    // basketEL.classList.remove('show')
    hideBasket()
})

// 복잡한 로직을 간단하게 함수로 "추상화" 했다
// 장바구니 보여주기 
function showBasket(){
    basketEL.classList.add('show')
}
// 장바구니 사라지게 하기 
function hideBasket(){
    basketEL.classList.remove('show')
}


// 검색!!!
const headerEl = document.querySelector('header')
// ... : 전개 연산자 spread operator
// 전개 연산자를 이용한 얕은 복사 shallow copy
const headerMenuEls = [...headerEl.querySelectorAll('ul.menu > li')]
const searchWrapEl = headerEl.querySelector('.search-wrap')
const searchStarterEl = headerEl.querySelector('.search-starter')
const searchCloserEl = searchWrapEl.querySelector('.search-closer')
const searchShadowEl = searchWrapEl.querySelector('.shadow')
const searchInputEl = searchWrapEl.querySelector('input')
const searchDelayEls = [...searchWrapEl.querySelectorAll('li')]

// searchStarterEl.addEventListener('click', function () {
//     showSearch()
// })

//  더 깔금하게 코드 작성하기 
// 자바스크립트 part 에서 더 자세하게 공부필요!
searchStarterEl.addEventListener('click', showSearch)
searchCloserEl.addEventListener('click', hideSearch)
searchShadowEl.addEventListener('click', hideSearch)

function showSearch() {
    headerEl.classList.add('searching')
    document.documentElement.classList.add('fixed')
    // 순차적으로 사라지도록 만들었다. 
    headerMenuEls.reverse().forEach(function (el, index) {
        //  index 숫자는 0 부터 시작한다. 
        el.style.transitionDelay = index * .4 / headerMenuEls.length + 's'
    })
    searchDelayEls.forEach(function (el, index) {
        el.style.transitionDelay = index * .4 / searchDelayEls.length + 's'
    })
    setTimeout(function () {
        searchInputEl.focus()
    }, 600)
}
function hideSearch() {
    headerEl.classList.remove('searching')
    // 검색바가 나타나면 화면이 고정되도록 만들었다.
    document.documentElement.classList.remove('fixed')
    headerMenuEls.reverse().forEach(function (el, index) {
        el.style.transitionDelay = index * .4 / headerMenuEls.length + 's'
    })
    searchDelayEls.reverse().forEach(function (el, index) {
        el.style.transitionDelay = index * .4 / searchDelayEls.length + 's'
    })
    // 원래 상태로 다시 뒤집어 준다
    searchDelayEls.reverse()
    // 검색창 초기화
    searchInputEl.value = ''
}





// swiper
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 4,
    spaceBetween: 30,
    centeredSlides: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });
  
  var swiper = new Swiper('.mySwiper', {
      slidesPerView: 3,
    /* swiper-slide에 각각 margin-right를 준다. */
    spaceBetween: 20,
    /* 전체적인 슬라이드의 왼쪽에 20px 공백을 준다. */
      slidesOffsetBefore: 20,
    /* 전체적인 슬라이드의 오른쪽에 20px 공백을 준다. */
    slidesOffsetAfter: 20,
    pagination: {
        el: '.swiper-pagination',
      clickable: true,
    }
  })
  
  
  var swiper = new Swiper(".mySwiper1", {
    slidesPerView: 4,
    spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination1",
      clickable: true,
    },
  });
  
  
  /**
   * 페이지 스크롤에 따른 요소 제어
   */
  // 페이지 스크롤에 영향을 받는 요소들을 검색!
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
  
  /**
   * 부유하는 요소 관리
   */
  // 범위 랜덤 함수(소수점 2자리까지)
  function random(min, max) {
    // `.toFixed()`를 통해 반환된 '문자 데이터'를,
    // `parseFloat()`을 통해 소수점을 가지는 '숫자 데이터'로 변환
    return parseFloat((Math.random() * (max - min) + min).toFixed(2))
  }
  // 부유하는(떠 다니는) 요소를 만드는 함수
  function floatingObject(selector, delay, size) {
    gsap.to(
      selector, // 선택자
      random(1.5, 2.5), // 애니메이션 동작 시간
      {
        delay: random(0, delay), // 얼마나 늦게 애니메이션을 시작할 것인지 지연 시간을 설정.
        y: size, // `transform: translateY(수치);`와 같음. 수직으로 얼마나 움직일지 설정.
        repeat: -1, // 몇 번 반복하는지를 설정, `-1`은 무한 반복.
        yoyo: true, // 한번 재생된 애니메이션을 다시 뒤로 재생.
        ease: Power1.easeInOut // Easing 함수 적용.
      }
    )
  }
  floatingObject('.floating1', 1, 15)
  floatingObject('.floating2', .5, 15)
  floatingObject('.floating3', 1.5, 20)
  
  
  /**
   * 요소가 화면에 보여짐 여부에 따른 요소 관리
   */
  // 관리할 요소들 검색!
  const spyEls = document.querySelectorAll('section.scroll-spy')
  // 요소들 반복 처리!
  spyEls.forEach(function (spyEl) {
    new ScrollMagic
      .Scene({ // 감시할 장면(Scene)을 추가
        triggerElement: spyEl, // 보여짐 여부를 감시할 요소를 지정
        triggerHook: .8 // 화면의 80% 지점에서 보여짐 여부 감시
      })
      .setClassToggle(spyEl, 'show') // 요소가 화면에 보이면 show 클래스 추가
      .addTo(new ScrollMagic.Controller()) // 컨트롤러에 장면을 할당(필수!)
  })
  
  
  
  // new Swiper('.awards .swiper-container', {
  //   // direction: 'horizontal', // 수평 슬라이드
  //   autoplay: true, // 자동 재생 여부
  //   loop: true, // 반복 재생 여부
  //   spaceBetween: 30, // 슬라이드 사이 여백
  //   slidesPerView: 5, // 한 번에 보여줄 슬라이드 개수
  //   // slidesPerGroup: 5, // 한 번에 슬라이드 할 개수(전체 개수로 나뉘어야 함)
  //   navigation: { // 슬라이드 이전/다음 버튼 사용 여부
  //     prevEl: '.awards .swiper-prev', // 이전 버튼 선택자
  //     nextEl: '.awards .swiper-next' // 다음 버튼 선택자
  //   }
  // })