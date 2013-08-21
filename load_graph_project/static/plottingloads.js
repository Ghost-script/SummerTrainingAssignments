/*
 * JQuery script for managing the radio buttons and plotting the graphics.
 *
 * Using Flot library and it's time plugin.
 *
 * Arnau Orriols, 2013.
 */


$(document).ready(function(){

    $("input:radio[name=selectby]").change(function (){

        /* Manage inputs on radio buttons change */
        if ($(this).is("#time")){
            $("#day_for_time_span").show().children().prop("required", true);
            $("#selection_span").children().attr({
                pattern :"(([0-1][0-9])|(2[0-4]))(/|-|\\.|:|')?(([0-5][0-9])|(60))?", 
                title : "Time string, like: '23' or '23:05'"
            });

        } else {

            /* if the button selected is date or all */
            $("#day_for_time_span").hide().children().prop("required", false);
            $("#selection_span").children().attr({
                pattern : "(((20)[1-9][0-9])(/|-|\\.|:|')?(((0[1-9])|(1[0-2]))(/|-|\\.|:|')?(([0-2][0-9])|(3[0-1]))?)?)",
                title : "Date string, like: '2013' or '2013/08' or '2013-08-21'"
            });
        }

        if (!$(this).is("#all")){
            $("#selection_span").show().children().prop("required", true);

        } else {
            $("#selection_span").hide().children().prop("required", false);
        }
    });

    /* render graphic */
    $.plot($("#plot"),
           [plot_data1, plot_data2, plot_data3],
           {
               xaxis : {mode : "time"},
               legend : {
                            show : true,
                            position : "ne",
                            margin : 10
                        }
           });

});
