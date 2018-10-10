$( document ).ready(function() {
    $('.skills-carousel').owlCarousel({
        loop:true,
        margin:30,
        nav:true,
        rtl:true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:2
            }
        }
    });
    if (window.languageCode == 'ar') {
        rtl = true
    } else {
        rtl = false
    }
    // Main Story Slider
    $(".main-story").slick({
        autoplay: true,
        autoplaySpeed:5000,
        dots: true,
        arrows:false,
        slidesToShow: 1,
        slidesToScroll: 1,
        rtl: rtl
    });

    $( ".story-slide" ).children('img').each(function(n, img){
        var $img = $(img);
        var $imgUrl = $(this).attr('src');
        $img.parent('.story-slide').css({
            'background': 'transparent url(' + $imgUrl + ') center center no-repeat',
            'background-size': 'cover',
            '-webkit-background-size': 'cover',
            '-moz-background-size': 'cover',
            '-o-background-size': 'cover'
        });
        $img.hide();
    });

    // Rector Slider / Client Testimonial
//  $(".kku-rector-slider").slick({
//      dots: true,
//      arrows:false,
//      slidesToShow: 1,
//      slidesToScroll: 1,
//      adaptiveHeight:true
//  });
    //
    $(".kku-rector-slider-1").slick({
        dots:false,
        arrow:false,
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: '.kku-rector-slider-2',
        rtl: rtl
    });
    $(".kku-rector-slider-2").slick({
        dots:true,
        arrow:false,
        slidesToShow: 1,
        slidesToScroll: 1,
        asNavFor: '.kku-rector-slider-1',
        adaptiveHeight:true,
        rtl: rtl
    });

    //


    // test property
    $('.welcom-block').matchHeight({
        property: 'min-height'
    });
     //tooltip
     $('[data-toggle="tooltip"]').tooltip();

    //brand logo slider
    $('.our-partners ul').slick({
          dots: true,
          infinite: false,
          speed: 300,
          slidesToShow: 4,
          slidesToScroll: 1,
          rtl: rtl,
          responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 3,
                infinite: true,
                dots: true
              }
            },
            {
              breakpoint: 767,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 3
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 3
              }
            }
          ]
        });
    $('.search-toggle').click(function(){
        $('.search input[type=search]').slideToggle();
    });
    var subscribe = function(event) {
      var emailId = $(".newsform input[type='email']").val();
      var $success = $(".newsform .success");
      var $error = $(".newsform .error");
      $success.addClass("hidden");
      $error.addClass("hidden");
      $.ajax({
        url: '/subscribe/',
        method: 'POST',
        data: {email_id: emailId},
        success: function(message){
          $(".newsform .success").html(message.message)
          $(".newsform .success").removeClass("hidden")
        }
      });
    }
    $('.newsform-button').bind('click', subscribe);
});

var equalheight = function(container){

  var currentTallest = 0,
       currentRowStart = 0,
       rowDivs = new Array(),
       $el,
       topPosition = 0,
       currentDiv = 0;
   $(container).each(function() {

     $el = $(this);
     $($el).height('auto')
     var topPostion = $el.position().top;

     if (currentRowStart != topPostion) {
       for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
         rowDivs[currentDiv].height(currentTallest);
       }
       rowDivs.length = 0; // empty the array
       currentRowStart = topPostion;
       currentTallest = $el.height();
       rowDivs.push($el);
     } else {
       rowDivs.push($el);
       currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
    }
     for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
       rowDivs[currentDiv].height(currentTallest);
     }
   });
}

 $(window).load(function(){
     if ($(window).width() >= 767) {
    	 equalheight('.featured-block');
     }
});

$(window).resize(function(){
  if ($(window).width() >= 767) {
    equalheight('.featured-block');
  }
});
