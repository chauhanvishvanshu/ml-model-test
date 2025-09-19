document.getElementById('predictForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const species = document.getElementById('species').value;
  const count = document.getElementById('count').value;
  const length = document.getElementById('length').value;

  const payload = { species, count, length_cm: length };

  const resultDiv = document.getElementById('result');
  resultDiv.textContent = '⏳ Predicting...';

  try {
    const res = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (res.ok) {
      resultDiv.textContent = `✅ Predicted Size Class: ${data.predicted_size_class}`;
    } else {
      resultDiv.textContent = `❌ Error: ${data.error || JSON.stringify(data)}`;
    }
  } catch (err) {
    resultDiv.textContent = '❌ Request failed — is the Flask backend running?';
  }
});
