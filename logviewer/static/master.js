$(document).ready( function() {
    var present = false;
    $(window).scroll( function (){
        if ($("#home").offset().top < $(window).scrollTop()){
            if (present == false){
                $("#nav_menu").append($("<a></a>").attr({
                    
                    "id" : "arrow_back",
                    "href" : "javascript:return_up()"
                }).css({
                        "width" : "70px",
                        "font-size" : "5em",
                        "position" : "fixed",
                        "left" : "20px",
                        "bottom" : "20px",
                        "text-align" : "center"
                    }).text('\u034e'));
            present = true;
            }
        } else {
            if (present == true){
                $("#arrow_back").remove();
                present = false;
            }
        }
    });
});

function return_up (){
    $("html, body").animate({scrollTop : 0}, "fast");
}
