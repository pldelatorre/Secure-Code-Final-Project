const gameContainer = document.getElementById('game');
const restartButton = document.getElementById('reset-btn');
const cardImages = [
    'pictures/catjpg.jpg', 'pictures/catjpg.jpg',
    'pictures/batpng.png', 'pictures/batpng.png',
    'pictures/cow.jpg', 'pictures/cow.jpg',
    'pictures/giraffjpg.jpg', 'pictures/giraffjpg.jpg',
    'pictures/lionjpg.jpg', 'pictures/lionjpg.jpg',
    'pictures/otterpng.png', 'pictures/otterpng.png',
    'pictures/panda.png', 'pictures/panda.png',
    'pictures/rabbit.png', 'pictures/rabbit.png',
    'pictures/snakepng.png', 'pictures/snakepng.png',
    'pictures/squirallpng.png', 'pictures/squirallpng.png'
];

let card1 = null;
let card2 = null;
let lockBoard = false;
let matchedCards = 0;

// Shuffle function
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Create the cards
function createCards() {
    shuffle(cardImages);
    cardImages.forEach(image => {
        const card = document.createElement('li');
        card.classList.add('card');
        card.innerHTML = `<img src="${image}" alt="Card Image">`;
        card.addEventListener('click', flipCard);
        gameContainer.appendChild(card);
    });
}

// flip function
function flipCard() {
    if (lockBoard) return;
    if (this === card1) return;

    this.classList.add('flipped');

    if (!card1) {
        card1 = this;
        return;
    }

    card2 = this;
    lockBoard = true;
    checkForMatch();
}

// Check for match
function checkForMatch() {
    const isMatch = card1.innerHTML === card2.innerHTML;

    if (isMatch) {
        matchedCards += 2;
        card1.classList.add('matched');
        card2.classList.add('matched');
        resetBoard();
    } else {
        setTimeout(() => {
            card1.classList.remove('flipped');
            card2.classList.remove('flipped');
            resetBoard();
        }, 1000);
    }
}

// Reset the board
function resetBoard() {
    [card1, card2, lockBoard] = [null, null, false];
    if (matchedCards === cardImages.length) {
        setTimeout(() => {
            alert("You've won!");
            // Show the highscore form (new addition)
            document.getElementById('highscore-form').style.display = 'block';
        }, 500);
    }
}

// Restart the game
function restartGame() {
    gameContainer.innerHTML = '';
    matchedCards = 0;
    document.getElementById('highscore-form').style.display = 'none'; // Hide form on restart
    createCards();
}

// Event listener for the restart button
restartButton.addEventListener('click', restartGame);

// Initial game setup
createCards();

// Hypothetical Highscore Submission 
document.getElementById('highscore-form').addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission

    const playerName = document.getElementById('player-name').value;
    const score = matchedCards / 2; // Calculate score (number of pairs)

    localStorage.setItem('highscore_name', playerName);
    localStorage.setItem('highscore_score', score);

    console.log(`Sending high score: Name = ${playerName}, Score = ${score}`);

    // For this example, we'll just display a message:
    alert(`High score submitted! Name: ${playerName}, Score: ${score}`);
    //  Hide the form after submission
    document.getElementById('highscore-form').style.display = 'none';
    //  Restart the game?
    restartGame(); 
});