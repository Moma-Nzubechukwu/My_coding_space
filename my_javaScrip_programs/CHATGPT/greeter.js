// greeter.js

// Function to greet the user
function greetUser(name) {
    console.log(`Hello, ${name}!`);
}

// Ask for the user's name
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('What is your name? ', (name) => {
    greetUser(name);
    readline.close();
});
