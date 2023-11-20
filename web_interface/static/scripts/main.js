    import * as utils from "./utils.js";
    import * as translation from "./translate.js";


    window.addEventListener("load", (event) => main(event));

    function main (event) {
        //update time each minute
        setInterval(updateTime, 6000);
        event.preventDefault();
        let res =  fetchDb.getCurrentState()

        //connect with db

    }

    function updateTime () {
        //Get current date and time
        const dateElement = document.querySelector("#date");
        const timeElement = document.querySelector("#time");

        let result = utils.getTime(); 

        dateElement.textContent = result.currentDay;
        timeElement.textContent = result.time;
    }



    //show time on 1st upload
    updateTime();

    const translateElement = document.querySelector("#language");
    translateElement.addEventListener("click", (ev) => translation.translate(ev));