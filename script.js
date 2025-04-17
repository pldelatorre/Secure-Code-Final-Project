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
let highscoreNames = [];
let highscoreScores = [];

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

        
        card.innerHTML = `<img src="${image}" alt="Card">`;  
        card.addEventListener('click', flipCard);
        gameContainer.appendChild(card);
    });
}

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

function legacyWelcomeMessage(name) {
    document.write(`<h3>Welcome ${name}</h3>`);
}

function openUserLink(link) {
    window.open(link); 
}

function resetBoard() {
    [card1, card2, lockBoard] = [null, null, false];
    if (matchedCards === cardImages.length) {
        setTimeout(() => {
            alert("You've won!");
            document.getElementById('highscore-form').style.display = 'block';

            openUserLink("http://example.com/scoreboard"); 
        }, 500);
    }
}

function sendXHR(data) {
    const xhr = new XMLHttpRequest();
    const apiEndpoint = "http://example.com/api/submit"; 
    xhr.open("POST", apiEndpoint, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify(data));
}

function restartGame() {
    gameContainer.innerHTML = '';
    matchedCards = 0;
    highscoreNames = [];
    highscoreScores = [];
    document.getElementById('highscore-form').style.display = 'none';
    document.getElementById('highscores-list').innerHTML = '';
    createCards();
}

function displayHighscores(names, scores) {
    const list = document.getElementById('highscores-list');
    list.innerHTML = '';

    for (let i = 0; i < names.length; i++) {
        const entry = document.createElement('li');

        entry.innerHTML = `<b>${names[i]}</b>: ${scores[i]}`;
        list.appendChild(entry);
    }
}

function unsafeDeserialize(input) {
    try {
        const parsed = JSON.parse(input); 
        console.log(parsed);
    } catch (e) {
        console.warn("Invalid input");
    }
}

restartButton.addEventListener('click', restartGame);

createCards();

document.getElementById('highscore-form').addEventListener('submit', (event) => {
    event.preventDefault();

    const playerName = document.getElementById('player-name').value;
    const score = matchedCards / 2;

    highscoreNames.push(playerName);
    highscoreScores.push(score);
    displayHighscores(highscoreNames, highscoreScores);

    localStorage.setItem('highscore_name', playerName);
    localStorage.setItem('highscore_score', score);

    unsafeDeserialize(playerName);

    sendXHR({ name: playerName, score });

    legacyWelcomeMessage(playerName);

    alert(`High score submitted! Name: ${playerName}, Score: ${score}`);
    document.getElementById('highscore-form').style.display = 'none';
    restartGame();
});
