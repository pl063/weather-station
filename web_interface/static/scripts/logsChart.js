
  
    //add translation to logs page
      import * as translation from "./translate.js";
      const translateElement = document.querySelector("#language");
      translateElement.addEventListener("click", (ev) => translation.translate(ev));

      main();

     async function main() {
      //get entries for today
        await fetch("/logs/entries")
        .then(response=>response.json())
        .then( function drawData(data) {
          let entries = JSON.parse(data);
          console.log(entries)
          new Chart(
            document.getElementById("chart"), //context for the chart
            {
              type: "line",
              data: {
                //x labels
                labels: entries.map(el => {
                  let timestamp = el.created_at; 
                  let date = new Date(timestamp * 1000);
                  let hrs = date.getHours();
                  let mins = date.getMinutes();
                  Number(mins) < 10 ? mins = `0${mins}` : mins ;
                  let formattedTime =  hrs + ':' + mins;
                  return formattedTime
                }),
                datasets: [
                  {
                    label: "Temperature °C",
                    //y label
                    data: entries.map (el => el.temperature),
                    cubicInterpolationMode: "monotone",
                    borderColor: "rgb(183, 28, 28)",
                    //fill: true,
                  },
                  {
                    label: "Humidity %",
                    //y
                    data: entries.map (el => el.humidity),
                    cubicInterpolationMode: "monotone",
                    borderColor: "rgb(28, 183, 183)",
                    //fill: true,
                  },
                ]
              },
            }
          );
        })
    }
