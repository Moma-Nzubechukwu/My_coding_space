// subwaySurfers.js

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let playerPosition = 0;
let obstacles = [5, 10, 15, 20];
let score = 0;

function playGame() {
    console.log(`You are at position ${playerPosition}. Score: ${score}`);
    console.log("Obstacles ahead: " + obstacles.filter(obstacle => obstacle > playerPosition).join(", "));
    readline.question('Do you want to jump (j) or run (r)? ', (action) => {
        if (action === 'j') {
            playerPosition += 2;
            score++;
            console.log("You jumped!");
        } else if (action === 'r') {
            playerPosition += 1;
            score++;
            console.log("You ran!");
        } else {
            console.log("Invalid action!");
        }

        if (obstacles.includes(playerPosition)) {
            console.log("Game over! You hit an obstacle.");
            console.log(`Final score: ${score}`);
            readline.close();
        } else if (playerPosition >= 25) {
            console.log("You reached the end of the track! Congratulations!");
            console.log(`Final score: ${score}`);
            readline.close();
        } else {
            playGame();
        }
    });
}

playGame();
