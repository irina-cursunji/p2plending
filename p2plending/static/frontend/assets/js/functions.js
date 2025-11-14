$(document).ready(function() {
  // Initialize WOW.js for animations
  new WOW().init();

  // Sticky header effect
  $(window).scroll(function() {
      var scroll = $(window).scrollTop();
      if (scroll >= 200) {
          $(".header").addClass("head-tag-sticky");
      } else {
          $(".header").removeClass("head-tag-sticky");
      }
  });

  // Mobile menu toggle
  $("header .mob-menu-icon").on('click', function() {
      $('body').toggleClass('show-menu');
      $('.menu-mobile').toggleClass('menu-active');
  });

  $('.mob-menu .closebtn').on('click', function() {
      $('body').removeClass('show-menu');
      $('.menu-mobile').removeClass('menu-active');
  });

  $('.menu-mobile > ul > li').on('click', function() {
      $(this).children('ul').slideToggle();
  });

  // Counter animation
  $(window).scroll(function() {
      var hT = $('.counterbox').offset().top,
          hH = $('.counterbox').outerHeight(),
          wH = $(window).height(),
          wS = $(this).scrollTop();

      if (wS > (hT + hH - wH)) {
          $('.counterdigi').each(function() {
              var $this = $(this),
                  countTo = $this.attr('data-count');

              $({
                  countNum: $this.text()
              }).animate({
                  countNum: countTo
              }, {
                  duration: 2000,
                  easing: 'swing',
                  step: function() {
                      $this.text(Math.floor(this.countNum));
                  },
                  complete: function() {
                      $this.text(this.countNum);
                  }
              });
          });
      }
  });

  // Smooth scroll for internal links
  $('a[href^="#"]').on('click', function(event) {
      event.preventDefault();
      var target = $(this.getAttribute('href'));
      if (target.length) {
          $('html, body').stop().animate({
              scrollTop: target.offset().top
          }, 1000);
      }
  });

  // Parallax effect
  $(window).on('scroll', function() {
      var scrollPos = $(this).scrollTop();
      $('.parallax').each(function() {
          var $this = $(this);
          var offset = $this.data('offset');
          $this.css('background-position', 'center ' + (scrollPos * offset) + 'px');
      });
  });
});
