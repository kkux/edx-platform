$(document).ready(function(){
    $(".usermenu").click(function(){
        $(this).toggleClass("open");
        $(this).children(".dropdown-menu").toggleClass("hidden");
    });
    $('.navbar-toggle').click(function(){
        if($(".navbar-collapse").hasClass('collapse in')){
            $(".navbar-collapse").removeClass("in");
        }
        else{
            $(".navbar-collapse").addClass("in");
        }
    });
    $('.search-toggle').click(function(){
        $('.search input[type=search]').slideToggle();
    });
});
$(document).on("click", function(event){
    var $trigger = $(".usermenu");
    if($trigger !== event.target && !$trigger.has(event.target).length){
        $(".usermenu").removeClass("open");
        $(".usermenu .dropdown-menu").addClass("hidden");
    }
});
