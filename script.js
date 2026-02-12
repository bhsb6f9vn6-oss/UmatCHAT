async function ask() {
  const url = document.getElementById("url").value;
  const question = document.getElementById("question").value;

  const res = await fetch("https://YOUR-BACKEND.onrender.com/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url, question })
  });

  const data = await res.json();
  document.getElementById("response").innerText = data.answer;
}
