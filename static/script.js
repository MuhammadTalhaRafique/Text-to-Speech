function convertText() {
    let text = document.getElementById("text-input").value;
    
    if (text.trim() === "") {
        alert("Please enter text to convert to speech.");
        return;
    }

    fetch('/speak', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.audio_url) {
            let audioPlayer = document.getElementById("audio-player");
            audioPlayer.src = data.audio_url;
            audioPlayer.style.display = "block";
            audioPlayer.play();
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => console.error("Error:", error));
}
