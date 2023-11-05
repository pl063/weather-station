
    function getTime () {
 
        let date = new Date();

        let day = date.getDate();
        let shortMonth = date.toLocaleString("en-us", { month: "short" });
        let year = date.getFullYear();
        let currentDay = `${day} ${shortMonth} ${year}`;

        let time = `${date.getHours()}:${date.getMinutes()}`;

        return {currentDay, time}
    }

    function counter (timer) {
    let resultFlag = false;
        try {
            let i = 0; 
            timer = Number(timer)

            while (i < timer) {
                //if i is 1 step close to timer
                if(i+1 === timer) {
                    resultFlag = true;
                }
                i++;
            }

        }
        catch {
            throw new Error("Invalid param type, expected Number.");
        }
        
        return resultFlag
    }

    export {getTime, counter}