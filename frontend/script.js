const form = document.getElementById('predictForm');
const resultEl = document.getElementById('result');
const predictBtn = form.querySelector('button[type="submit"]');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  predictBtn.disabled = true;
  predictBtn.textContent = "Predicting...";

  const species = document.getElementById('species').value;
  const count = +document.getElementById('count').value;
  const length_cm = +document.getElementById('length').value;

  const payload = { species, count, length_cm };

  resultEl.textContent = "⏳ Waiting for prediction…";

  try {
    const res = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (res.ok) {
      resultEl.textContent = `✅ Predicted Size Class: ${data.predicted_size_class}`;
    } else {
      resultEl.textContent = `❌ Error: ${data.error || "Something went wrong"}`;
    }
  } catch (err) {
    resultEl.textContent = "❌ Request failed — is the backend running?";
  } finally {
    predictBtn.disabled = false;
    predictBtn.textContent = "Predict";
  }
});
