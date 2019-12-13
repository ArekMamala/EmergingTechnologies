var mousePressed = false;
var lastX, lastY;
var ctx;
var canvas = document.getElementById('myCanvas')

//var context = canvas.getContext('2d');

function InitThis() {
    ctx = document.getElementById('myCanvas').getContext("2d");

    $('#myCanvas').mousedown(function (e) {
        mousePressed = true;
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
    });

    $('#myCanvas').mousemove(function (e) {
        if (mousePressed) {
            Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
        }
    });

    $('#myCanvas').mouseup(function (e) {
        mousePressed = false;
    });
    $('#myCanvas').mouseleave(function (e) {
        mousePressed = false;
    });
}

function Draw(x, y, isDown) {
    if (isDown) {
        ctx.beginPath();
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 5;
        ctx.lineJoin = "round";
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.stroke();
    }
    lastX = x;
    lastY = y;
}

function clearArea() {
    // Use the identity matrix while clearing the canvas
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}


function Predict() {
    var canvas = document.getElementById('myCanvas');
    var url = "digit";
    var dataURL = canvas.toDataURL();
    var imageData = canvas.toDataURL();


    $.post(url, {
        "imageBase64": imageData
    }, function (data) {
        $("#predictedNumber").empty().append(data);
        console.log('saved');

    });
}
