    import * as utils from "./utils.js"

    window.addEventListener("load", (event) => main(event));

   function main (event) {
    //update time each minute
    setInterval(updateTime, 6000);
    event.preventDefault();
    }

    function updateTime () {
        //Get current date and time
        const dateElement = document.querySelector("#date");
        const timeElement = document.querySelector("#time");

        let result = utils.getTime(); 

        dateElement.textContent = result.currentDay;
        timeElement.textContent = result.time;
    }

    updateTime();