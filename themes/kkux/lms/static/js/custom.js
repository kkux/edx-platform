$( document ).ready(function() {
	$('.skills-carousel').owlCarousel({
		loop:true,
		margin:30,
		nav:true,
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
	// test property
	$('.welcom-block').matchHeight({
		property: 'min-height'
	});
	$('.featured-block .image').matchHeight({
		property: 'min-height'
	});
	$('.skills-details h3').matchHeight({
		property: 'min-height'
	});
	$('.skills-details p').matchHeight({
		property: 'min-height'
	});
	$('.upcoming').matchHeight({
		property: 'min-height'
	});
	$('.featured-block').matchHeight({
		property: 'min-height'
	});
	$(".usermenu").click(function(){
        $(this).toggleClass("open");
        $(this).children(".dropdown-menu").toggleClass("hidden");
    });
});
$(document).on("click", function(event){
    var $trigger = $(".usermenu");
    if($trigger !== event.target && !$trigger.has(event.target).length){
        $(".usermenu").removeClass("open");
        $(".usermenu .dropdown-menu").addClass("hidden");
    }            
});
