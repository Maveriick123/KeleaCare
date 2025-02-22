async function sendMessage() {
    const inputField = document.querySelector(".chat-input input");
    const message = inputField.value;
    if (!message) return;  // Evita enviar mensajes vacíos

    const response = await fetch("http://127.0.0.1:8000/api/send-message/", {
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

async function sendMessageChat() {
    const inputField = document.querySelector(".chat-input input"); // Selecciona el input correctamente
    const chatMessages = document.querySelector(".chat-messages");
    const messageText = inputField.value.trim(); // Captura el mensaje y elimina espacios vacíos

    if (!messageText) return; // Evita enviar mensajes vacíos

    // Crear el elemento de mensaje del usuario
    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "message-user"); // Aplica clases CSS
    userMessage.innerHTML = `<div class="message-content">${messageText}</div>`;

    // Agregar el mensaje al chat
    chatMessages.appendChild(userMessage);

    // Desplazar automáticamente hacia abajo para mostrar el último mensaje
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Limpiar el campo de entrada
    inputField.value = "";
}

document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".chat-input button").addEventListener("click", sendMessageChat);
});

document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.querySelector("#theme-toggle");
    const chatContainer = document.querySelector("#chatContainer");
    const chatHeader = document.querySelector(".chat-header");

    // Obtener el valor de data-background en index.html
    const backgroundImage = chatContainer.getAttribute("data-background");

    themeToggle.addEventListener("change", function () {
        if (themeToggle.checked) {
            // 🔹 Aplica la imagen de corazones SOLO si el switch está activado
            chatContainer.style.backgroundImage = `url('${backgroundImage}')`;

            // Cambia el color de los mensajes del usuario
            document.querySelectorAll(".message-user").forEach(msg => {
                msg.style.backgroundColor = "#C70039"; // Rojo oscuro
            });

            // Cambia el color del fondo de la cabecera
            chatHeader.style.backgroundColor = "#C70039"; // Rojo oscuro

        } else {
            // 🔹 Quita el fondo cuando el switch está desactivado
            chatContainer.style.backgroundImage = "none";

            // Restaura el color original de los mensajes del usuario (azul)
            document.querySelectorAll(".message-user").forEach(msg => {
                msg.style.backgroundColor = "#6a82fb"; // Azul original
            });

            // Restaura el color original de la cabecera (azul)
            chatHeader.style.backgroundColor = "#6a82fb"; // Azul original
        }
    });
});
