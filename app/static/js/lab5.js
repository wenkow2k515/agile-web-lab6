async function wordle() {
    try {
        const guess = document.getElementById("guess").value;
        const response = await fetch(`https://drtnf.net/wordle_guess?guess=${guess}`);
        const data = await response.json();
        const outcome = data.outcome;

        const answerElement = document.getElementById("answer");
        answerElement.innerHTML = ""; // Clear previous results

        // Render the outcome
        outcome.forEach((value, index) => {
            const span = document.createElement("span");
            span.textContent = guess[index];
            if (value === 2) {
                span.style.color = "green"; // Correct letter and position
            } else if (value === 1) {
                span.style.color = "orange"; // Correct letter, wrong position
            } else {
                span.style.color = "gray"; // Letter not present
            }
            answerElement.appendChild(span);
        });
    } catch (error) {
        console.error("Error in wordle function:", error);
    }
}
async function updateTimeLeft() {
    try {
        const response = await fetch("https://drtnf.net/wordle_time_left");
        const data = await response.json();
        const timeLeft = data.time_left;

        const hintElement = document.getElementById("hint");
        hintElement.textContent = `Time left for the current word: ${timeLeft} seconds`;
    } catch (error) {
        console.error("Error in updateTimeLeft function:", error);
    }
}


// Update the time left every second
setInterval(updateTimeLeft, 1000);