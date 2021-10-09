const API_KEY = "dc112664b734973e12fe221508a38ebe";
//https://home.openweathermap.org/api_keys

function onGeoOk(position) {
  //navigator.geolocation.getCurrentPosition(onGeoOk,onGeoError)이후에
  //console.log(position)적고 f12로 확인해 보셈 인자 나옴

  const lat = position.coords.latitude; //위도
  const lon = position.coords.longitude; //경도
  console.log("님 여기삼", lat, lon);
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`;
  // https://api.openweathermap.org/data/2.5/weather?lat=35.190192&lon=128.1270761&appid=dc112664b734973e12fe221508a38ebe&units=metric

  console.log(url);
  //API 호출은 https://openweathermap.org/current 에 By geographic coordinates에서 확인
  fetch(url).then(response => response.json()).then(data => {
    const weather = document.querySelector("#weather span:nth-child(1)");
    const city = document.querySelector("#weather span:nth-child(2)");
    const wind_speed = document.querySelector("#weather span:nth-child(4)");
    const temp = document.querySelector("#weather span:nth-child(5)");
    const humid = document.querySelector("#weather span:nth-child(6)");
    const wind_deg = document.querySelector("#weather span:nth-child(7)");

    weather.innerText = `${data.weather[0].main}`;
    city.innerText = String(`현재 장소는 ${data.name}입니다\n`);
    wind_speed.innerText = String(`현재 풍속은 ${data.wind.speed}\n`);
    temp.innerText = String(`현재 온도는 ${data.main.temp}도\n`);
    humid.innerText = String(`습도는 ${data.main.humidity}% 입니다\n`);

    //날씨별 색깔변화

    if ((weather.innerText = "Clear")) {
      document.querySelector("#background-weather").src = "/static/img/clear.jpg";
    }
    if ((weather.innerText = "Clouds")) {
      document.querySelector("#background-weather").src = "/static/img/clouds.jpg";
    }
		else{
			alert("날씨인자 없음")
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
      wind_deg.innerText = "남동이 불고 있습니다";
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
