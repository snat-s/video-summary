const input = document.getElementById("linkInput");
const submitButton = document.getElementById("submitButton");
const response = document.getElementById("response");

submitButton.addEventListener("click", () => {
    const link = input.value;
    input.value = "";
    response.innerHTML = "Loading...";
    /*
      Make a loading for the input.
     */
    fetch("http://localhost:8888/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ link })
    })
        .then(res => res.json())
        .then(data => {
            response.innerHTML = data.message;
        })
        .catch(error => {
            response.innerHTML = "An error occurred.";
            console.error(error);
        });
});
