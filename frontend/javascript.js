var url = "http://127.0.0.1:5000/view";
var id = "view";

async function generator(url, id) {
  var request = await new XMLHttpRequest();

  request.open("GET", url, true);
  request.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response);
    view(data, request, id);
  };

  request.send();
}

function view(data, request, id) {
  if (id == "view") {
    if (request.status >= 200 && request.status < 400) {
      data.forEach((query) => {
        console.log(request.status);
        var div = document.createElement("tr");
        var mainContainer = document.getElementById(id);
        div.innerHTML =
          "<td>" +
          query.id +
          "</td><td><input id='gyarto" +
          query.id +
          "' placeholder='" +
          query.gyarto +
          "' value='" +
          query.gyarto +
          "'/></td><td><input id='tipus" +
          query.id +
          "' placeholder='" +
          query.tipus +
          "' value='" +
          query.tipus +
          "'/></td><td><input id='evjarat" +
          query.id +
          "' placeholder='" +
          query.evjarat +
          "' value='" +
          query.evjarat +
          "'/></td>  <td><input id='szin" +
          query.id +
          "' placeholder='" +
          query.szin +
          "' value='" +
          query.szin +
          "'/></td> <td><input id='ajtok_szama" +
          query.id +
          "' placeholder='" +
          query.ajtok_szama +
          "' value='" +
          query.ajtok_szama +
          "'/></td>" +
          "<button onclick = 'deleterecord(" +
          query.id +
          ")' type = 'submit' value='Submit'>Törlés</button>" +
          "<button onclick = 'update(" +
          query.id +
          ")'>Frissités</button>";
        mainContainer.appendChild(div);
      });
    } else {
      console.log("error");
    }
  }
}

async function generate_html() {
  await generator(url, id);
}

function deleterecord(id) {
  const data = JSON.stringify({
    id: parseInt(id),
  });

  navigator.sendBeacon("http://127.0.0.1:5000/deleterecord/", data);
  console.log(data);
}
function update(id) {
  const data = JSON.stringify({
    id: id,
    gyarto: document.getElementById("gyarto" + id).value,
    tipus: document.getElementById("tipus" + id).value,
    evjarat: document.getElementById("evjarat" + id).value,
    szin: document.getElementById("szin" + id).value,
    ajtok_szama: document.getElementById("ajtok_szama" + id).value,
  });

  navigator.sendBeacon("http://127.0.0.1:5000/updatedetails/", data);
  console.log(data);
}

generate_html();
