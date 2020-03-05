$(function($) {

    'use strict';

    /*-----------------------------------------------------------------
     * Variables
     *-----------------------------------------------------------------*/

    var $body_html = $('body, html'),
        $html = $('html'),
        $body = $('body'),

        $navigation = $('#navigation'),
        navigation_height = $navigation.height() - 20,

        $scroll_to_top = $('#scroll-to-top'),

        $preloader = $('#preloader'),
        $loader = $preloader.find('.loader');

    if (navigation_height <= 0) navigation_height = 60;

    /*-----------------------------------------------------------------
     * Is mobile
     *-----------------------------------------------------------------*/

    var ua_test = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i,
        is_mobile = ua_test.test(navigator.userAgent);

    $html.addClass(is_mobile ? 'mobile' : 'no-mobile');

    /*-----------------------------------------------------------------
     * Background Parallax
     *-----------------------------------------------------------------*/

    $.stellar({
        responsive: true,
        horizontalOffset: 0,
        verticalOffset: 0,
        horizontalScrolling: false,
        hideDistantElements: false
    });

    /*-----------------------------------------------------------------
     * ScrollSpy
     *-----------------------------------------------------------------*/

    $body.scrollspy({
        offset:  51,
        target: '#navigation'
    });

    /*-----------------------------------------------------------------
     * Affixed Navbar
     *-----------------------------------------------------------------*/

    $('.affix').affix({
        offset: {
            top: navigation_height
        }
    });

    /*-----------------------------------------------------------------
     * Dropdown By Click on Mobile
     *-----------------------------------------------------------------*/

    if (is_mobile) {
        $('.dropdown-toggle').each(function() {
            $(this).attr('data-toggle', 'dropdown');
        });
    }

    /*-----------------------------------------------------------------
     * Scroll To Top
     *-----------------------------------------------------------------*/

    $(window).scroll(function () {

        var $scroll_top = $(this).scrollTop();

        if ($scroll_top > navigation_height) {
            $scroll_to_top.addClass('in');
        } else {
            $scroll_to_top.removeClass('in');
        }
    });

    $scroll_to_top.click(function() {
        $.scrollWindow(0);
    });

    /*-----------------------------------------------------------------
     * Smooth Scrolling
     *-----------------------------------------------------------------*/

    $('a[href^="#"]').click(function(event) {

        event.preventDefault();

        var $this = $(this),
            target = $this.attr('href');

        // Don't return false!
        if (target == '#') return;

        if ($this.hasClass('smooth-scroll')) {
            var offset = $(target).offset().top - navigation_height;
            $.scrollWindow(offset);
        }
    });

    $.scrollWindow = function(offset) {
        $body_html.animate({
            scrollTop: offset
        }, 1500);
    };

    /*-----------------------------------------------------------------
     * Animation
     *-----------------------------------------------------------------*/

    // Init WOW
    new WOW().init({ mobile: false });


    /*-----------------------------------------------------------------
     * Magnific
     *-----------------------------------------------------------------*/

    $('.image-popup').magnificPopup({
        closeBtnInside : true,
        type           : 'image',
        mainClass      : 'mfp-with-zoom'
    });

    $('.iframe-popup').magnificPopup({
        type      : 'iframe',
        mainClass : 'mfp-with-zoom'
    });

    /*-----------------------------------------------------------------
     * Carousels
     *-----------------------------------------------------------------*/

    // Home Page Slider
    $(".slider").owlCarousel({
        singleItem            : true,
        responsive            : true,
        autoHeight            : true,

        mouseDrag             : false,
        touchDrag             : false,

        responsiveRefreshRate : 0,
        transitionStyle       : 'fadeUp'
    });

    // Home Page Testimonials Carousel
    $("#testimonials-carousel").owlCarousel({
        pagination        : false,
        navigation        : true,
        responsive        : true,
        autoPlay          : false,

        paginationSpeed   : 400,
        slideSpeed        : 300,

        items             : 7,
        itemsDesktop 	  : [1100, 7],
        itemsDesktopSmall : [880,5],
        itemsMobile 	  : [550,3],

        navigationText    : [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>'
        ]
    });

    // Project carousel

    // Set Thumbs for Images
    var setThumbs = function() {
        $.each(this.owl.userItems, function(i) {
            $('.owl-controls .owl-page').eq(i).css({
                'background': 'url(' + $(this).find('img').attr('src') + ')',
                'background-size': 'cover'
            })
        });
    };

    // Init carousel
    $(".project-carousel").owlCarousel({
        pagination        : true,
        navigation        : true,
        responsive        : true,
        singleItem        : true,
        autoPlay          : false,

        paginationSpeed   : 400,
        slideSpeed        : 300,

        itemsDesktop 	  : [1199, 3],
        itemsDesktopSmall : [991,2],
        itemsMobile 	  : [590,1],
        transitionStyle   : 'fadeUp',

        afterInit         : setThumbs,
        afterUpdate       : setThumbs,

        navigationText    : [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>'
        ]
    });

    // Recent Projects
    $(".projects-carousel").owlCarousel({
        pagination        : false,
        navigation        : true,
        responsive        : true,
        autoPlay          : false,

        paginationSpeed   : 400,
        slideSpeed        : 300,

        items             : 4,
        itemsDesktop 	  : [1199, 4],
        itemsDesktopSmall : [991,2],
        itemsMobile 	  : [590,1],
        navigationText    : [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>'
        ]
    });

    // Clients
    $(".clients-carousel").owlCarousel({
        pagination        : false,
        navigation        : true,
        responsive        : true,
        autoPlay          : false,

        paginationSpeed   : 400,
        slideSpeed        : 300,

        items             : 4,
        itemsDesktop 	  : [1199, 4],
        itemsDesktopSmall : [991,2],
        itemsMobile 	  : [590,1],
        navigationText    : [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>'
        ]
    });


    /*-----------------------------------------------------------------
     * Finish loading
     *-----------------------------------------------------------------*/

    $(window).load(function() {

        /* Remove preloader */

        $loader.delay(1500).fadeOut();
        $preloader.delay(500).fadeOut('slow');

        $body.addClass('loaded');

    });

});
