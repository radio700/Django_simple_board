const API_KEY = "dc112664b734973e12fe221508a38ebe";
//https://home.openweathermap.org/api_keys

function onGeoOk(position) {
  //navigator.geolocation.getCurrentPosition(onGeoOk,onGeoError)이후에
  //console.log(position)적고 f12로 확인해 보셈 인자 나옴

  const lat = position.coords.latitude; //위도
  const lon = position.coords.longitude; //경도
  // console.log("님 여기삼", lat, lon);
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
  // https://api.openweathermap.org/data/2.5/weather?lat=35.190192&lon=128.1270761&appid=dc112664b734973e12fe221508a38ebe&units=metric

  console.log(url);
  //API 호출은 https://openweathermap.org/current 에 By geographic coordinates에서 확인
  fetch(url).then(response => response.json()).then(data => {
    const city = document.querySelector("#weather div.w1");
    const weather = document.querySelector("#weather div.w2");
    const wind_speed = document.querySelector("#weather div.w3");
    const temp = document.querySelector("#weather div.w4");
    const humid = document.querySelector("#weather div.w5");
    const wind_deg = document.querySelector("#weather div.w6");

    
    document.querySelector("#weather span.lat7").innerText = position.coords.latitude;
    document.querySelector("#weather span.lon8").innerText = position.coords.longitude;
    city.innerText = String(`현재 계신 곳 : ${data.name}시\n`);
    weather.innerText = String(`${data.weather[0].main}`);
    wind_speed.innerText = String(`현재 풍속은 ${data.wind.speed}m/s\n`);
    temp.innerText = String(`현재 온도는 ${data.main.temp}도\n`);
    humid.innerText = String(`습도는 ${data.main.humidity}% 입니다\n`);
    // glat.innerText = `${lat}`
    // glon.innerText = `${lon}`

    //날씨별 색깔변화

    if (weather.innerText == "Clear") {
      document.querySelector("#background-weather").src = "/static/img/clear.jpg";
      document.querySelector("#wicon").src = "/static/img/icon_clear.png";
      weather.innerText = "날씨 : 맑음\n";
    }
    else if (weather.innerText == "Clouds") {
      document.querySelector("#background-weather").src = "/static/img/clouds.jpg";
      document.querySelector("#wicon").src = "/static/img/icon_cloud.png";
      weather.innerText = "날씨 : 구름낌\n";
    }
    else if (weather.innerText == "Rain") {
      document.querySelector("#background-weather").src = "/static/img/Rain.jpg";
      document.querySelector("#wicon").src = "/static/img/icon_rain.png";
      weather.innerText = "날씨 : 비\n";
    }
    else {
      alert("날씨인자 없음");
    }

    // Clouds	Mist	Smoke	Haze	Dust	Fog	Sand	Dust	Ash	Squall	Tornado
    // Snow	Rain	Drizzle	Thunderstorm

    //wind
    wind_deg.innerText = data.wind.deg;
    if (data.wind.deg < 90) {
      wind_deg.innerText = "북서풍이 불고 있습니다";
    } else if (data.wind.deg == 90) {
      wind_deg.innerText = "동풍이 불고 있습니다";
    } else if ((data.wind.deg > 90) & (data.wind.deg < 180)) {
      wind_deg.innerText = "남동풍이 불고 있습니다";
    } else if (data.wind.deg == 180) {
      wind_deg.innerText = "남풍이 불고 있습니다";
    } else if (data.wind.deg > 180 && data.wind.deg < 270) {
      wind_deg.innerText = "남서풍이 불고 있습니다";
    } else if (data.wind.deg == 270) {
      wind_deg.innerText = "서풍이 불고 있습니다";
    } else if ((data.wind.deg > 270) & (data.wind.deg < 360)) {
      wind_deg.innerText = "북서풍이 불고 있습니다";
    } else if (data.wind.deg == 360) {
      wind_deg.innerText = "북풍이 불고 있습니다";
    }
  });
}

function onGeoError() {
  alert("NULL");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
