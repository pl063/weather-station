    
    const dataScheme = require("../database_setup/schemas.cjs");

    async function retrieveLastEntry (database) {
        let current_timestamp = Number(new Date().getTime());
        //console.log("***" + current_timestamp)
        //current_timestamp = current_timestamp - 1800000;
        //console.log(current_timestamp)
        try {
            let data = await database.model("current_days", dataScheme).find({
                created_at: {$lte: current_timestamp}
            });
            //console.log(data[data.length - 1])
            let databaseObj = data[data.length - 1]
            if (databaseObj) {
                return databaseObj
            } else {
                throw new Error("No entry found for dashboard.")
            }
        } catch (error) {
            console.log(error);
            return {
                temperature: "N/A",
                humidity: "N/A",
                pressure: "N/A",
                rain: "N/A"
            }
        }
    };

    module.exports = retrieveLastEntry;