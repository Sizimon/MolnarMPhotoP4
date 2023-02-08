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
            $('#myModal').css('display', 'block')
            $('#imgModal').attr('src', this.src)
            $('.navbar').css('display', 'none')
        })
        /* Favourite image functionality */
        /*
        var favouriteImages = []
        
        imgSrc = $(this).attr('src', this.src);
        $('#favourites-btn').click(function () {
            favouriteImages.push(imgSrc)
        }) */
    })
    $('.close').each(function() {
        $(this).click(function() {
            $('#myModal').css('display', 'none')
            $('.navbar').css('display', 'flex')
        })
    })
})
/*
favouriteImages.forEach(function() {
    $('#favourites-gal').append(<img class='myImg'/>)
})
*/
