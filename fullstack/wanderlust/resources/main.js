// Foursquare API Info
const clientId = 'ZEPB15XV31OU0R2MFBJAJZ0JLG5ZPNH5LV42Q3ICC0TNUWLA';
const clientSecret = 'UW4DNUOOJVWNHAYFHR3012HJ2TMPM3UOXX5J4RFZ11DS1UGY';
const url = 'https://api.foursquare.com/v2/venues/explore?near=';//api call with query key near

// OpenWeather Info
const openWeatherKey = 'fd746abef0f5255024c4842a6012b17f';
const weatherUrl = 'https://api.openweathermap.org/data/2.5/weather';

// Page Elements
const $input = $('#city');
const $submit = $('#button');
const $destination = $('#destination');
const $container = $('.container');
const $venueDivs = [$("#venue1"), $("#venue2"), $("#venue3"), $("#venue4")];
const $weatherDiv = $("#weather1");
const weekDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

// Add AJAX functions here:
const getVenues = async () => {
    const city = $input.val();
    const urlToFetch = url + city +"&limit=10%client_id=" + clientId + "&client_secret=" + 
    clientSecret + "&v=20210626";

    try {
        const response = await fetch(urlToFetch);
        if ((response).ok) {
            console.log(response);
        }
    } catch(error) {
        console.log(error);
    }

}

const getForecast = () => {

}


// Render functions
const renderVenues = (venues) => {
  $venueDivs.forEach(($venue, index) => {
    // Add your code here:

    let venueContent = '';
    $venue.append(venueContent);
  });
  $destination.append(`<h2>${venues[0].location.city}</h2>`);
}

const renderForecast = (day) => {
  // Add your code here:
  
	let weatherContent = '';
  $weatherDiv.append(weatherContent);
}

const executeSearch = () => {
  $venueDivs.forEach(venue => venue.empty());
  $weatherDiv.empty();
  $destination.empty();
  $container.css("visibility", "visible");
  getVenues()
  getForecast()
  return false;
}

$submit.click(executeSearch)