document.getElementById('predictForm').addEventListener('submit', async function(e){
  e.preventDefault();
  const species = document.getElementById('species').value;
  const count = document.getElementById('count').value;
  const length = document.getElementById('length').value;
  const payload = {species, count, length_cm: length};
  document.getElementById('result').textContent = 'Predicting...';
  try{
    const res = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if(res.ok){
      document.getElementById('result').textContent = `Prediction: ${data.prediction} (${data.label})`;
    } else {
      document.getElementById('result').textContent = 'Error: ' + (data.error||JSON.stringify(data));
    }
  } catch(err){
    document.getElementById('result').textContent = 'Request failed — is the Flask backend running?';
  }
});