// subwaySurfers.js

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let playerPosition = 0;
let obstacles = [5, 10, 15, 20];
let score = 0;
let roadLength = 25;

function drawRoad() {
    let road = "";
    for (let i = 0; i < roadLength; i++) {
        if (i === playerPosition) {
            road += "P"; // Player
        } else if (obstacles.includes(i)) {
            road += "X"; // Obstacle
        } else {
            road += "-"; // Road
        }
    }
    console.log(road);
}

function playGame() {
    console.clear();
    drawRoad();
    console.log(`Score: ${score}`);
    readline.question('Do you want to jump (j) or run (r)? ', (action) => {
        if (action === 'j') {
            if (playerPosition + 2 < roadLength) {
                playerPosition += 2;
                score++;
            }
        } else if (action === 'r') {
            if (playerPosition + 1 < roadLength) {
                playerPosition += 1;
                score++;
            }
        }

        if (obstacles.includes(playerPosition)) {
            console.clear();
            drawRoad();
            console.log("Game over! You hit an obstacle.");
            console.log(`Final score: ${score}`);
            readline.close();
        } else if (playerPosition >= roadLength - 1) {
            console.clear();
            drawRoad();
            console.log("You reached the end of the track! Congratulations!");
            console.log(`Final score: ${score}`);
            readline.close();
        } else {
            playGame();
        }
    });
}

playGame();
