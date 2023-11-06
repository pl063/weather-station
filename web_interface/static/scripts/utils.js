
    function getTime () {
 
        let date = new Date();

        let day = date.getDate();
        let shortMonth = date.toLocaleString("en-us", { month: "short" });
        let year = date.getFullYear();
        let currentDay = `${day} ${shortMonth} ${year}`;

        let time = `${date.getHours()}:${date.getMinutes()}`;

        return {currentDay, time}
    }


    export {getTime}