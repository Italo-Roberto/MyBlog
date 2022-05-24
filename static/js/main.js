$(document).ready(function () {
    $('#cont1').hide()
    $('#cont2').hide()

    $('#btn1').click(function () { 
        $('#cont1').toggle('slow')
    });
    $('#btn2').click(function () { 
        $('#cont2').toggle('slow')
    });
});

//Scroll reaver
ScrollReveal().reveal('#person', { delay: 400 })
ScrollReveal().reveal('.eu', { delay: 250 })
ScrollReveal().reveal('.skill-header', { delay: 250 })
ScrollReveal().reveal('.skill-container', { delay: 400 })
ScrollReveal().reveal('#port-head', { delay: 250 })
ScrollReveal().reveal('.slide', { delay: 400 })
ScrollReveal().reveal('#blog-head', { delay: 250 })
ScrollReveal().reveal('.posts', { delay: 400 })
ScrollReveal().reveal('#contato-head', { delay: 250 })
ScrollReveal().reveal('.contact-container', { delay: 400 })

var atual = new Date
var anoBody = document.getElementById('anoBody')
anoBody.innerHTML = atual.getFullYear()
