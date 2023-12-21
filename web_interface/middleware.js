
    import { MongoClient } from "mongodb";
    import { DATABASE_URL } from "./conf.js";

    const client = new MongoClient(DATABASE_URL);
    const db = client.db("Weather");
    const current_days = db.collection("current_days");
    const current_weeks = db.collection("current_weeks");

    async function retrieveLastEntry () {
        try {
            // const query = {created_at: {$gte: current_timestamp}};
            const options = {
                sort: {created_at: -1}
            };
            let data = await current_days.find({}, options).toArray();
            //console.log(data)
           // console.log(data[0])
            let databaseObj = data[0];
            if (databaseObj) {
                return databaseObj
            } else {
                console.log("No entry found for dashboard.")
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

    async function retrieveEntries () {
        //let current_timestamp = Number(new Date().getTime());
        //let day_border = current_timestamp - 86400000;
        try {
            let data = await current_days.find({}).toArray();
            //console.log(data);
            return data
        } catch (err) {
            console.log(err);
        }
    }

    async function migrate () {
        try {
            let data = await current_days.find({}).toArray();
            current_weeks.insertMany(data);

            current_days.deleteMany({})
        } catch (err) {
            console.log(err);
        }
    }

  export const middleware = {
        retrieveLastEntry, 
        retrieveEntries
    }
