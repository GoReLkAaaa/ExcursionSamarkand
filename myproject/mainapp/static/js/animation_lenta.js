const track = document.querySelector('.carousel-track');
let isPaused = false;
let position = 0;
const speed = 1;

function moveTrack() {
    if (!isPaused) {
        position -= speed;
        if (Math.abs(position) >= track.scrollWidth / 2) {
            position = 0;
        }
        track.style.transform = `translateX(${position}px)`;
    }
    requestAnimationFrame(moveTrack);
}


track.addEventListener('mouseover', () => {
    isPaused = true;
});


track.addEventListener('mouseout', () => {
    isPaused = false;
});


moveTrack();

// Вторая функция
const track_2 = document.querySelector('.carousel-track_2');
let isPaused_2 = false;
let position_2 = -10;
const speed_2 = 1;

function moveTrack_2() {
    if (!isPaused_2) {
        position_2 += speed_2;
        if (position_2 >= track_2.scrollWidth / 2) {
            position_2 = 0;
        }
        track_2.style.transform = `translateX(${position_2}px)`;
    }
    requestAnimationFrame(moveTrack_2);
}


track_2.addEventListener('mouseover', () => {
    isPaused_2 = true;
});


track_2.addEventListener('mouseout', () => {
    isPaused_2 = false;
});


moveTrack_2();



const track_3 = document.querySelector('.carousel-track_3');
let isPaused_3 = false;
let position_3 = 0;
const speed_3 = 2;

function moveTrack_3() {
    if (!isPaused_3) {
        position_3 -= speed_3;
        if (Math.abs(position_3) >= track_3.scrollWidth / 2) {
            position_3 = 0;
        }
        track_3.style.transform = `translateX(${position_3}px)`;
    }
    requestAnimationFrame(moveTrack_3);
}


track_3.addEventListener('mouseover', () => {
    isPaused_3 = true;
});


track_3.addEventListener('mouseout', () => {
    isPaused_3 = false;
});


moveTrack_3();
