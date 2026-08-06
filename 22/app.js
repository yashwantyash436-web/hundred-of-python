const map = L.map('map').setView([12.2958,76.6394],13);

L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png').addTo(map);

// 📍 Locations
const locations = {
  "Kuvempunagar":[12.2958,76.6394],
  "Vijayanagar":[12.307,76.649],
  "Gokulam":[12.315,76.655],
  "Hebbal":[12.305,76.66],
  "Jayanagar":[12.28,76.65],
  "Nazarbad":[12.27,76.64],
  "Metagalli":[12.31,76.62],
  "Chamrajpura":[12.295,76.68],
  "Infosys":[12.32,76.65],
  "MIT":[12.31,76.66]
};

const fromSelect = document.getElementById("from");
const toSelect = document.getElementById("to");
const resultBox = document.getElementById("result");

// Fill dropdown
for(let place in locations){
  fromSelect.innerHTML += `<option>${place}</option>`;
  toSelect.innerHTML += `<option>${place}</option>`;
}

// 🚌 Icon
const busIcon = L.icon({
  iconUrl:'https://img.icons8.com/color/96/bus.png',
  iconSize:[40,40]
});

let routeLine, userMarker, buses = [], interval;

// 🎤 Voice
function startVoice(){
  try{
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const rec = new SpeechRecognition();

    rec.lang = "en-IN";
    rec.start();

    rec.onresult = (e)=>{
      let text = e.results[0][0].transcript.toLowerCase();

      let found = Object.keys(locations).filter(p =>
        text.includes(p.toLowerCase())
      );

      if(found.length >= 2){
        fromSelect.value = found[0];
        toSelect.value = found[1];
      }
    };
  }catch(e){
    alert("Voice not supported");
  }
}

// 🚀 MAIN FUNCTION
async function findBus(){

  clearAll();

  let from = locations[fromSelect.value];
  let to = locations[toSelect.value];

  userMarker = L.marker(from).addTo(map).bindPopup("📍 You").openPopup();

  resultBox.innerText = "🤖 AI analyzing buses, traffic, routes...";

  // ROUTE API
  let url = `https://router.project-osrm.org/route/v1/driving/${from[1]},${from[0]};${to[1]},${to[0]}?overview=full&geometries=geojson`;

  let res = await fetch(url);
  let data = await res.json();

  let coords = data.routes[0].geometry.coordinates.map(c=>[c[1],c[0]]);

  routeLine = L.polyline(coords,{color:'red'}).addTo(map);
  map.fitBounds(routeLine.getBounds());

  // 🚌 MULTIPLE BUSES
  for(let i=0;i<4;i++){

    let crowd = ["Empty","Moderate","Crowded"][Math.floor(Math.random()*3)];
    let traffic = ["Low","Medium","High"][Math.floor(Math.random()*3)];

    let startIndex = Math.floor(Math.random()*coords.length);

    let marker = L.marker(coords[startIndex],{icon:busIcon}).addTo(map);

    marker.bindPopup(
      `🚌 Bus ${i+1}<br>
       👥 Crowd: ${crowd}<br>
       🚦 Traffic: ${traffic}`
    );

    buses.push({
      marker,
      index:startIndex,
      crowd,
      traffic
    });
  }

  // 🤖 AI selection
  let best = buses.find(b=>b.crowd==="Empty" && b.traffic!=="High")
          || buses.find(b=>b.crowd==="Moderate")
          || buses[0];

  let num = buses.indexOf(best)+1;

  resultBox.innerText =
    `🤖 AI Recommendation:
     🚌 Bus ${num}
     👥 Crowd: ${best.crowd}
     🚦 Traffic: ${best.traffic}
     ✔ Best balance of comfort & speed`;

  // 🚀 MOVEMENT
  interval = setInterval(()=>{

    buses.forEach(bus=>{

      let current = coords[bus.index];
      let next = coords[bus.index+1];

      if(!next) return;

      let distToUser = map.distance(current, from);

      let speed = distToUser < 150 ? 0.0003 : 0.0008;

      let trafficFactor =
        bus.traffic === "High" ? 0.5 :
        bus.traffic === "Medium" ? 0.7 : 1;

      let lat = current[0] + (next[0]-current[0]) * speed * trafficFactor;
      let lng = current[1] + (next[1]-current[1]) * speed * trafficFactor;

      bus.marker.setLatLng([lat,lng]);

      if(Math.random() > 0.4){
        bus.index++;
      }

    });

  },800);
}

// CLEAR
function clearAll(){
  if(routeLine) map.removeLayer(routeLine);
  if(userMarker) map.removeLayer(userMarker);

  buses.forEach(b=>map.removeLayer(b.marker));
  buses = [];

  if(interval) clearInterval(interval);
}