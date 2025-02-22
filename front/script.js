async function sendMessage() {
    const inputField = document.querySelector(".chat-input"); 
    const message = inputField.value;  
    if (!message) return;  // Evita enviar mensajes vacíos

    const response = await fetch("http://127.0.0.1:8000/send-message/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: message }),
    });

    const data = await response.json();
    console.log(data); 
}


function toggleHistory() {
    var history = document.querySelector('.chat-history');
    var chat = document.querySelector('.chat-container');
    var openHistory = document.querySelector('.open-history');
    if (history.classList.contains("hidden")) {
        history.classList.remove("hidden");
        chat.classList.remove("fullscreen");
        openHistory.style.display = "none";
    } else {
        history.classList.add("hidden");
        chat.classList.add("fullscreen");
        openHistory.style.display = "block";
    }
}
