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
        ctx.lineWidth = 9;
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


function PredictNumber() {
    //directed to take the image
    var canvas = document.getElementById("myCanvas");
    var dataURL = canvas.toDataURL();
    console.log(dataURL);

    // Using Ajax post method for the image
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:5000/digit',
        data: {
            imgBase64: dataURL
        }
    }).done(function (data) {
        // Logging to the console to confirm
        console.log('SENT');
        // sending predicted number to the console
        console.log(data);
        $("#predict").empty().append(data);
    });
};

function sendImage() {
    var canvas = document.getElementById('myCanvas');
    var url = "http://127.0.0.1:5000/digit";
    var dataURL = canvas.toDataURL();
    var imageData = canvas.toDataURL();


    $.post(url, {
        "imageBase64": imageData
    }, function (data) {
        $("#predict").empty().append(data);
        console.log('saved');

    });
}
