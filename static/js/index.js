$(document).ready(function(){
    // Smooth scrolling for navigation links
    $('a.nav-link').on('click', function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function(){
                window.location.hash = hash;
            });
        }
    });

    // Fade in effect for the container
    gsap.from('.container', {duration: 1, opacity: 0, y: -50});

    // Bounce effect for the navbar brand
    gsap.from('.navbar-brand', {duration: 1.5, opacity: 0, y: -50, ease: "bounce"});

    // Hover effect for buttons
    $('.btn-primary').hover(function() {
        gsap.to(this, {duration: 0.3, scale: 1.1});
    }, function() {
        gsap.to(this, {duration: 0.3, scale: 1});
    });

    // Hover effect for the navbar brand with cursor area color change
    $('.navbar-brand').hover(function(event) {
        gsap.to(this, {duration: 0.3, scale: 1.1});
        $(this).css('color', '#0056b3');
    }, function() {
        gsap.to(this, {duration: 0.3, scale: 1});
        $(this).css('color', '#007bff');
    });

    // Slide in effect for nav links
    gsap.from('.nav-link', {duration: 1, opacity: 0, x: -50, stagger: 0.2});

    // Scroll-triggered animations
    $(window).on('scroll', function() {
        $('.container').each(function() {
            if ($(this).offset().top < $(window).scrollTop() + $(window).height() - 100) {
                gsap.to(this, {duration: 1, opacity: 1, y: 0});
            }
        });
    });

    // Additional hover effects for buttons and links
    $('button, .nav-link').hover(function() {
        gsap.to(this, {duration: 0.3, scale: 1.1, backgroundColor: '#0056b3', color: '#ffffff'});
    }, function() {
        gsap.to(this, {duration: 0.3, scale: 1, backgroundColor: '', color: ''});
    });

    // Additional animations for buttons
    $('button').on('click', function() {
        gsap.to(this, {duration: 0.3, scale: 0.9});
        gsap.to(this, {duration: 0.3, scale: 1, delay: 0.3});
    });

    // Additional animations for navbar links
    $('.nav-link').on('click', function() {
        gsap.to(this, {duration: 0.3, scale: 0.9});
        gsap.to(this, {duration: 0.3, scale: 1, delay: 0.3});
    });

    // Fade in effect for images
    $('img').each(function() {
        gsap.from(this, {duration: 1, opacity: 0, y: 50});
    });

    // Rotate effect for icons
    $('.icon').hover(function() {
        gsap.to(this, {duration: 0.5, rotation: 360});
    }, function() {
        gsap.to(this, {duration: 0.5, rotation: 0});
    });

    // Pulse effect for call-to-action buttons
    $('.btn-cta').hover(function() {
        gsap.to(this, {duration: 0.3, scale: 1.2});
    }, function() {
        gsap.to(this, {duration: 0.3, scale: 1});
    });

    // Slide up effect for footer
    gsap.from('footer', {duration: 1, opacity: 0, y: 50});

    // Staggered fade in effect for list items
    $('ul li').each(function(index) {
        gsap.from(this, {duration: 1, opacity: 0, y: 20, delay: index * 0.1});
    });

    // Zoom in effect for cards
    $('.card').hover(function() {
        gsap.to(this, {duration: 0.3, scale: 1.05});
    }, function() {
        gsap.to(this, {duration: 0.3, scale: 1});
    });

    // Shake effect for error messages
    $('.alert-danger').each(function() {
        gsap.from(this, {duration: 0.5, x: -10, repeat: 5, yoyo: true});
    });

    // Expand effect for dropdown menus
    $('.dropdown-menu').on('show.bs.dropdown', function() {
        gsap.from(this, {duration: 0.3, height: 0});
    });

    // Collapse effect for dropdown menus
    $('.dropdown-menu').on('hide.bs.dropdown', function() {
        gsap.to(this, {duration: 0.3, height: 0});
    });

    // Fade in effect for modal
    $('.modal').on('show.bs.modal', function() {
        gsap.from(this, {duration: 0.5, opacity: 0, scale: 0.8});
    });

    // Fade out effect for modal
    $('.modal').on('hide.bs.modal', function() {
        gsap.to(this, {duration: 0.5, opacity: 0, scale: 0.8});
    });

    // Rotate effect for buttons on click
    $('button').on('click', function() {
        gsap.to(this, {duration: 0.3, rotation: 360});
    });

    // Slide in effect for sidebar
    $('.sidebar').hover(function() {
        gsap.to(this, {duration: 0.3, x: 0});
    }, function() {
        gsap.to(this, {duration: 0.3, x: -250});
    });

    // Fade in effect for tooltips
    $('[data-toggle="tooltip"]').on('show.bs.tooltip', function() {
        gsap.from(this, {duration: 0.3, opacity: 0});
    });

    // Fade out effect for tooltips
    $('[data-toggle="tooltip"]').on('hide.bs.tooltip', function() {
        gsap.to(this, {duration: 0.3, opacity: 0});
    });

    // Bounce effect for notifications
    $('.notification').each(function() {
        gsap.from(this, {duration: 1, y: -50, ease: "bounce"});
    });

    // Zoom in effect for profile pictures
    $('.profile-pic').hover(function() {
        gsap.to(this, {duration: 0.3, scale: 1.2});
    }, function() {
        gsap.to(this, {duration: 0.3, scale: 1});
    });

    // Slide down effect for accordions
    $('.accordion').on('show.bs.collapse', function() {
        gsap.from(this, {duration: 0.3, height: 0});
    });

    // Slide up effect for accordions
    $('.accordion').on('hide.bs.collapse', function() {
        gsap.to(this, {duration: 0.3, height: 0});
    });

    // Fade in effect for form fields
    $('form input, form textarea').each(function() {
        gsap.from(this, {duration: 0.5, opacity: 0, y: 20});
    });

    // Rotate effect for social media icons
    $('.social-icon').hover(function() {
        gsap.to(this, {duration: 0.5, rotation: 360});
    }, function() {
        gsap.to(this, {duration: 0.5, rotation: 0});
    });

    // Pulse effect for submit buttons
    $('form button[type="submit"]').hover(function() {
        gsap.to(this, {duration: 0.3, scale: 1.2});
    }, function() {
        gsap.to(this, {duration: 0.3, scale: 1});
    });
});