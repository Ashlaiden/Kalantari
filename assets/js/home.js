document.addEventListener("DOMContentLoaded", function () {
    var video = document.getElementById("background-video");
    var playPauseButton = document.getElementById("toggle-play");
    var muteButton = document.getElementById("toggle-mute");

    playPauseButton.addEventListener("click", function () {
        if (video.paused) {
            video.play();
            playPauseButton.innerHTML = '<i class="fa-solid fa-pause"></i>';
        } else {
            video.pause();
            playPauseButton.innerHTML = '<i class="fa-solid fa-play"></i>';
        }
    });

    muteButton.addEventListener("click", function () {
        if (video.muted) {
            video.muted = false;
            muteButton.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
        } else {
            video.muted = true;
            muteButton.innerHTML = '<i class="fa-solid fa-volume-xmark"></i>';
        }
    });
});