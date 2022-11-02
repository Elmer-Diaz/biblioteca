$(function () {

    // init feather icons
    feather.replace();


    /**Theme switcher - DEMO PURPOSE ONLY */
    $('.switcher-trigger').click(function () {
        $('.switcher-wrap').toggleClass('active');
    });
    $('.color-switcher ul li').click(function () {
        var color = $(this).attr('data-color');
        $("#theme-color").attr("href", "static/css/" + color + ".css");
        $('.color-switcher ul li').removeClass('active');
        $(this).addClass('active');

        console.log(color)

    });
});