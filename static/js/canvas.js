//context = document.getElementById('canvasInAPerfectWorld').getContext("2d");

var canvas = document.getElementById('canvasDiv');
var ctx = canvas.getContext("2d");
var painting = document.getElementById("content");
var paintStyle = getComputedStyle(painting);
canvas.width = parseInt(paintStyle.getPropertyValue("width"));
canvas.height = parseInt(paintStyle.getPropertyValue("height"));

var mouse = {x: 0, y: 0};

function clearcanvas1() {
    ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

download_img = function (el) {
    // get image URI from canvas object
    var imageURI = canvas.toDataURL("image/jpg");
    el.href = imageURI;
};

canvas.addEventListener('mousemove', function (e) {
    mouse.x = e.pageX - this.offsetLeft;
    mouse.y = e.pageY - this.offsetTop;
}, false);

//we define some proprties for the painting zone
ctx.lineWidth = 3;
ctx.lineJoin = 'round';
ctx.strokeStyle = '#000000';

canvas.addEventListener('mousedown', function (e) {
    //we draw the current path on canvas
    ctx.beginPath();
    ctx.moveTo(mouse.x, mouse.y);
    canvas.addEventListener('mousemove', onPaint, false);
}, false)

canvas.addEventListener('mouseup', function () {
    canvas.removeEventListener('mousemove', onPaint, false);
}, false);

var onPaint = function () {
    ctx.lineTo(mouse.x, mouse.y);
    ctx.stroke();
};


function sendImage() {
    var dataURL = canvas.toDataURL();

    $.ajax({
        type: "POST",
        url: "script.php",
        data: {
            imgBase64: dataURL
        }
    }).done(function (o) {
        console.log('saved');
        // If you want the file to be visible in the browser
        // - please modify the callback in javascript. All you
        // need is to return the url to the file, you just saved
        // and than put the image in your browser.
    });
}

