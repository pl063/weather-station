
    function getTime () {
 
        let date = new Date();

        let day = date.getDate();
        let shortMonth = date.getMonth();
        let year = date.getFullYear();
        let currentDay = `${day}/${shortMonth}/${year}`;

        let minutes = date.getMinutes();
        let displayMinutes = minutes < 10 ? `0${minutes}` : minutes
        let time = `${date.getHours()}:${displayMinutes}`;

        return {currentDay, time}
    }

    export {getTime}