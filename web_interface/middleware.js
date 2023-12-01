    
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
       
        //console.log(databaseObj)
        return databaseObj
    };

    module.exports = retrieveLastEntry;