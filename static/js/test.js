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





//new Swiper (선택자, 옵션)
new Swiper('.notice-line .swiper-container', {
  direction: 'vertical',
  autoplay: true,
  loop: true
  
});

new Swiper('.promotion .swiper-container', {
    // direction: 'horizontal', // 수평 슬라이드
    autoplay: { // 자동 재생 여부
      delay: 5000 // 5초마다 슬라이드 바뀜
    },
    loop: true, // 반복 재생 여부
    slidesPerView: 3, // 한 번에 보여줄 슬라이드 개수
    spaceBetween: 10, // 슬라이드 사이 여백
    centeredSlides: true, // 1번 슬라이드가 가운데 보이기
    pagination: { // 페이지 번호 사용 여부
      el: '.promotion .swiper-pagination', // 페이지 번호 요소 선택자
      clickable: true // 사용자의 페이지 번호 요소 제어 가능 여부
    },
    navigation: { // 슬라이드 이전/다음 버튼 사용 여부
      prevEl: '.promotion .swiper-prev', // 이전 버튼 선택자
      nextEl: '.promotion .swiper-next' // 다음 버튼 선택자
    }
  })



  var swiper = new Swiper(".mySwiper", {
    slidesPerView: 4,
    centeredSlides: true,
    spaceBetween: 30,
    grabCursor: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });
  
