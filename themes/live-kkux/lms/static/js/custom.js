debugger
$('.latest-p-slider').slick({
  dots: true,
  arrows: false,
  infinite: true,
  rtl:true,
  speed: 300,
  slidesToShow: 2,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

$('.about-kkux-slider').slick({
  dots: true,
  arrows: false,
  infinite: true,
  adaptiveHeight: true,
  rtl:true,
  speed: 300,
  slidesToShow: 1,
  slidesToScroll: 1
});

$('.success-part-slider').slick({
  dots: false,
  arrows: true,
  infinite: true,
  adaptiveHeight: true,
  rtl:true,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    }
  ]
});

$(document).ready(function() {
  $(' .login-details .search-btn ').click(function() {
    if (
      $(this)
        .next()
        .is(':visible')
    ) {
      $(this)
        .next()
        .slideUp();
    } else {
      $(this)
        .next()
        .slideDown();
    }
  });
});

$('.programs-views .latest-p-slider').slick('unslick');

$(function() {
  var filterList = {
    init: function() {
      $('#programslist').mixItUp({
        selectors: {
          target: '.portfolio',
          filter: '.filter'
        },
        load: {
          filter: '.all' // show app tab on first load
        }
      });
    }
  };

  // Run the show!
  filterList.init();
});

$(window).scroll(function() {
  var headerHeight = $('header').height();
  var programHeight = $('.program-filter').height();
  var totalHeight = headerHeight + programHeight;
  if ($(this).scrollTop() > totalHeight ) {
    $('.program-filter').addClass('sticky-filter');
  } else {
    $('.program-filter').removeClass('sticky-filter');
  }
});
