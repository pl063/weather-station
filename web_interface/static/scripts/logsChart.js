 

      //Set container of the chart, the type and settings
        const context = document.querySelector("#chart");
        const data = [
          { year: 2010, count: 10 },
          { year: 2011, count: 20 },
          { year: 2012, count: 15 },
          { year: 2013, count: 25 },
          { year: 2014, count: 22 },
          { year: 2015, count: 30 },
          { year: 2016, count: 28 },
        ];
        retrieveData();
        const chartConfig = {
          type: "line",
          data: {
            labels: data.map(row => row.year),
            datasets: [
              {
                label: 'Acquisitions by year',
                data: data.map(row => row.count)
                }
              ]
          },
          options: {
            responsive: true, 
            plugins: {

            }
          }
        };
   
      //draw the chart
      new Chart(context, chartConfig);


      async function retrieveData () {
        fetch("/logs/entries")
        .then (res => console.log(res))
      }

