
    import * as Text from "./dictionary.js"

    function translate (ev) {
        // find current language and page
        let dictionary;
        let currentLanguage = document.documentElement.lang;
        switch (currentLanguage) {
            case "en":
                dictionary = Text.bulgarianDictionary;
                document.documentElement.lang = "bg";
                break;
            case "bg":
                dictionary = Text.englishDictionary;
                document.documentElement.lang = "en";
                break;
            default:
                console.log("Unexpected language")
                break;
        }

       // translateHeader(dictionary);
        let allElements = document.querySelectorAll(".text");
        Array.prototype.filter.call(allElements, function(element){
            let currentText= element.textContent;
            element.textContent = dictionary[currentText];
          });
       



        // if(currentPage === "/dashboard") {
        //     translateDashboard(dictionary);
        // } else if (currentPage === "/logs") {
        //     translateLogs(dictionary);
        // } else {
        //     console.log("Unexpected page!")
        // }
       
        ev.preventDefault();
    }

    function translateDashboard(dictionary) {
        //find all elements

        
    }

    function translateLogs(dictionary) {

    }

    function translateHeader (dictionary) {
        const dashboardElement = document.querySelector("#dash-text");
        const logsElement = document.querySelector("#log-text");

        let currentDashText = dashboardElement.textContent;
        dashboardElement.textContent = dictionary[currentDashText];

        let currentLogText = logsElement.textContent;
        logsElement.textContent = dictionary[currentLogText];
    }
    export {translate}