// initialize and configuration for wow js - animations
wow = new WOW({
    animateClass: 'animated',
    offset: 150,
    mobile: false,
    live: true,
    callback: function(box) {
        //console.log("WOW: animating <" + box.tagName.toLowerCase() + ">")
    }
});
wow.init();

// initialize tooltips and popovers
$(function() {
    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle=popover]').popover();
})

$(window).scroll(function() {
    if ($(window).scrollTop() >= $(window).height()) {
        $('.header').addClass('fixed-header');
    } else {
        $('.header').removeClass('fixed-header');
    }
});


// js counters
$('#about-counter').bind('inview', function(event, visible, visiblePartX, visiblePartY) {
    if (visible) {
        $(this).find('.timer').each(function() {
            var $this = $(this);
            $({
                Counter: 0
            }).animate({
                Counter: $this.text()
            }, {
                duration: 2000,
                easing: 'swing',
                step: function() {
                    $this.text(Math.ceil(this.Counter));
                }
            });
        });
        $(this).unbind('inview');
    }
});

// smoth scroll
$(".nav li a[href^='#']").on('click', function(e) {
   // prevent default anchor click behavior
   e.preventDefault();

   // store hash
   var hash = this.hash;

   // animate
   $('html, body').animate({
       scrollTop: $(this.hash).offset().top
     }, 300, function(){

       // when done, add hash to url
       // (default click behaviour)
       window.location.hash = hash;
     });

});

//home slider
var swiper = new Swiper('.home-slider', {
    pagination: '.home-slider-pagination',
    paginationClickable: true,
    nextButton: '.home-slider-next',
    autoPlay: true,
    prevButton: '.home-slider-prev'
});

//testimonials slider
var swiper = new Swiper('.testimonials-slider', {
    pagination: '.testimonials-pagination',
    paginationClickable: true,
    slidesPerView: 1,
    spaceBetween: 30,
    nextButton: '.testimonials-slider-next',
    prevButton: '.testimonials-slider-prev'
});

//post slider
var swiper = new Swiper('.post-slider', {
    pagination: '.post-pagination',
    paginationClickable: true,
    nextButton: '.post-slider-next',
    prevButton: '.post-slider-prev',
    slidesPerView: 3,
    spaceBetween: 30,
    breakpoints: {
        1024: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        640: {
            slidesPerView: 1,
            spaceBetween: 30
        },
        320: {
            slidesPerView: 1,
            spaceBetween: 30
        }
    }
});




// swiper config for each offer slider (listings)
var swiper = new Swiper('.offer-slider', {
    // spaceBetween: 0,
    // observer:true,
    // observeParents:true
});

// allow to multiple instances of swiper one the one page / offer listing
$(".offer-slider").each(function(index, element) {
    var $this = $(this);
    $this.addClass("instance-" + index);
    $this.find(".offer-pagination-prev").addClass("btn-prev-" + index);
    $this.find(".offer-pagination-next").addClass("btn-next-" + index);
    var swiper = new Swiper(".instance-" + index, {
        // your settings ...
        spaceBetween: 0,
        spaceBetween: 0,
        observer: true,
        observeParents: true,
        nextButton: ".btn-next-" + index,
        prevButton: ".btn-prev-" + index,
    });
});

var swiper = new Swiper('.rooms-slider', {
    pagination: '.rooms-pagination',
    paginationClickable: true,
    slidesPerView: 4,
    spaceBetween: 30,
    nextButton: ".rooms-pagination-next",
    prevButton: ".rooms-pagination-prev",
    observer: true,
    observeParents: true,
    breakpoints: {
        1024: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        320: {
            slidesPerView: 1,
            spaceBetween: 0
        }
    }
});

var swiper = new Swiper('.flats-slider', {
    pagination: '.flats-pagination',
    paginationClickable: true,
    slidesPerView: 4,
    spaceBetween: 30,
    nextButton: ".flats-pagination-next",
    prevButton: ".flats-pagination-prev",
    observer: true,
    observeParents: true,
    breakpoints: {
        1024: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        320: {
            slidesPerView: 1,
            spaceBetween: 0
        }
    }
});

var swiper = new Swiper('.houses-slider', {
    pagination: '.houses-pagination',
    paginationClickable: true,
    slidesPerView: 4,
    spaceBetween: 30,
    nextButton: ".houses-pagination-next",
    prevButton: ".houses-pagination-prev",
    observer: true,
    observeParents: true,
    breakpoints: {
        1024: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 30
        },
        640: {
            slidesPerView: 2,
            spaceBetween: 30
        },
        320: {
            slidesPerView: 1,
            spaceBetween: 0
        }
    }
});

// Google maps configuration
// set your latitude, longitude and address of any point on Google Maps - http://www.gps-coordinates.net/
// Google maps reference - https://developers.google.com/maps/
// You need API key - https://developers.google.com/maps/documentation/javascript/get-api-key
// place your api key in link to script  <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
var map;
var mapAddress = new google.maps.LatLng(52.406374, 16.925168100000064);

function initialize() {

    var roadAtlasStyles = [{
        "featureType": "road.highway",
        "elementType": "geometry",
        "stylers": [{
            "saturation": -100
        }, {
            "lightness": -8
        }, {
            "gamma": 1.18
        }]
    }, {
        "featureType": "road.arterial",
        "elementType": "geometry",
        "stylers": [{
            "saturation": -100
        }, {
            "gamma": 1
        }, {
            "lightness": -24
        }]
    }, {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [{
            "saturation": -100
        }]
    }, {
        "featureType": "administrative",
        "stylers": [{
            "saturation": -100
        }]
    }, {
        "featureType": "transit",
        "stylers": [{
            "saturation": -100
        }]
    }, {
        "featureType": "water",
        "elementType": "geometry.fill",
        "stylers": [{
            "saturation": -100
        }]
    }, {
        "featureType": "road",
        "stylers": [{
            "saturation": -100
        }]
    }, {
        "featureType": "administrative",
        "stylers": [{
            "saturation": -100
        }]
    }, {
        "featureType": "landscape",
        "stylers": [{
            "saturation": -100
        }]
    }, {
        "featureType": "poi",
        "stylers": [{
            "saturation": -100
        }]
    }, {}]


    var mapOptions = {
        zoom: 15,
        scrollwheel: false,
        center: mapAddress,
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'usroadatlas']
        }
    };




    map = new google.maps.Map(document.getElementById('map-canvas'),
        mapOptions);

    var styledMapOptions = {

    };

    var marker = new google.maps.Marker({
        position: mapAddress,
        map: map,
    });

    var usRoadMapType = new google.maps.StyledMapType(
        roadAtlasStyles, styledMapOptions);

    map.mapTypes.set('usroadatlas', usRoadMapType);
    map.setMapTypeId('usroadatlas');
}

google.maps.event.addDomListener(window, 'load', initialize);