/* PREVENT DISPLAYING PAGE UNTIL LOADED */
$(document).ready(function() {
    document.getElementsByTagName("html")[0].style.visibility = "visible";
  });

/* NAVBAR CURRENT PAGE SETTING */
$(function() {
    var url = window.location.href;

    $("#navbarResponsive a").each(function() {
        if (url == (this.href)) {
            $(this).closest("li").addClass("active");
           $(this).closest("li").parent().parent().addClass("active");
        }
    });
});

/* IMAGE MODALS and FAVOURITE FUNCTIONALITY */

$(function() {
    $('.myImg').each(function() {
        $(this).click(function() {
            let modal = document.getElementById(this.nextElementSibling.id)
            $(modal).css('display', 'block')
            $(modal.firstElementChild).attr('src', this.src)
            $('.navbar').css('display', 'none')
        })
    })
    $('.close').each(function() {
        $(this).click(function() {
            let modal = document.getElementById(this.parentElement.id)
            $(modal).css('display', 'none')
            $('.navbar').css('display', 'flex')
        })
    })
})