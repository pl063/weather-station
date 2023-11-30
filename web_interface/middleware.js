    
    const dataScheme = require("../database_setup/schemas.cjs");

    async function retrieveLastEntry (database) {
        let current_timestamp = Number(new Date().getTime());
        //console.log("***" + current_timestamp)
        //current_timestamp = current_timestamp - 1800000;
        //console.log(current_timestamp)
        let data = await database.model("current_days", dataScheme).find({
            created_at: {$lte: current_timestamp}
        });
        //console.log(data[data.length - 1])
          if (!data) return;
        
        let databaseObj = data[data.length - 1]
        let x = Math.ceil(Number(databaseObj.pressure) / 1013.25)
        let altitude = 145366.45 * (1 -  Math.pow(x, 0.190284))
        console.log(altitude)
        Object.defineProperty(databaseObj, "altitude", {
            value: altitude
        });
       
        console.log(databaseObj)
        return databaseObj
    };

    module.exports = retrieveLastEntry;