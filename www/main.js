$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
        },
        out: {
            effect: 'fadeOutDown',
        }
    });
    
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: document.getElementById("siri-container").offsetWidth,
    height: 200,
style: "ios9",
amplitude: 1,
speed: 0.1,
autostart: true,

  });

  //siri
  $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync: true,
        },
        out: {
            effect: 'fadeOutUp',
            sync: true,
        }
    });


});
