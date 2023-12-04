    import * as utils from "./utils.js";
    import * as translation from "./translate.js";


    window.addEventListener("load", (event) => main(event));

    function main (event) {
        //update time each minute
        //getAltitude();
        setInterval(updateTime, 6000);
        event.preventDefault();
        updateImages();
        setInterval(function () {
        window.location.reload();
        //getAltitude();
        updateImages();
       }, 600000); 	//refresh page each 10 minutes
       

    }

    function updateTime () {
        //Get current date and time
        const dateElement = document.querySelector("#date");
        const timeElement = document.querySelector("#time");

        let result = utils.getTime(); 

        dateElement.textContent = result.currentDay;
        timeElement.textContent = result.time;
    }

    function updateImages () {
        let urlObj;

        const weatherIcon = document.querySelector("#icon");
        const temperatureElement = document.querySelector("#temperature");
        const rainElement = document.querySelector("#rain");

        //const backgroundElement = document.querySelector("body");

        //determine weather state

        let temperature = Number(temperatureElement.textContent.substring(0, 2));
        let rain = Number(rainElement.textContent);
        let rainFlag = false;
        if(rain === 1) {
            rainFlag = true;
        }

        let result;

        if (temperature <= 10 && temperature >= 0) {
            rainFlag 
            ? result = utils.updateImageUrl("rain") 
            :  result = utils.updateImageUrl("cold")
        } else if (temperature > 10 && temperature <=25) {
            rainFlag 
            ? result = utils.updateImageUrl("rain") 
            : result = utils.updateImageUrl()
        } else if (temperature > 25) {
            rainFlag 
            ? result = utils.updateImageUrl("rain") 
            : result = utils.updateImageUrl("hot")
        } else if (temperature < 0) {
            rainFlag 
            ? result = utils.updateImageUrl("snow") 
            : result = utils.updateImageUrl("cold")
        }
        weatherIcon.src = result.iconUrl;
        //backgroundElement.style.backgroundImage = `url(${result.backgroundUrl})`; 
    }

    function getAltitude () {
        const pressureElement = document.querySelector("#pressure");
        const altitudeElement = document.querySelector("#altitude");

        const pressure = Number(pressureElement.textContent.substring(0, 4));

        let altitude;
        let x = Math.ceil(Number(pressure) / 1013.25);
        isNaN(pressure) ? altitude = "N/A" : altitude = 145366.45 * (1 -  Math.pow(x, 0.190284));
       //console.log(altitude)
        altitudeElement.textContent = `${altitude}m`
    };
 


    //show time on 1st upload
    updateTime();

    const translateElement = document.querySelector("#language");
    translateElement.addEventListener("click", (ev) => translation.translate(ev));