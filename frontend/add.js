function sendPost() {
  const data = JSON.stringify({
    gyarto: document.getElementById("gyarto").value,
    tipus: document.getElementById("tipus").value,
    evjarat: document.getElementById("evjarat").value,
    szin: document.getElementById("szin").value,
    ajtok_szama: document.getElementById("ajtok_szama").value,
  });

  navigator.sendBeacon("http://127.0.0.1:5000/savedetails/", data);
  console.log(data);
}
