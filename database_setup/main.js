//Setup Mongo database with Node JS
    import mongoose from "mongoose";

    import * as conf from "./conf.js";
    import result from "./schemas.cjs";

    const username = encodeURIComponent(conf.USER.username);
    const password = encodeURIComponent(conf.USER.password);
    let uri =
    `mongodb+srv://${username}:${password}@weather-station.lllcyel.mongodb.net/Weather?retryWrites=true&w=majority`;

    console.log(uri);

    async function run() {

    try {
        const conn = await mongoose.createConnection(uri);
        const current_state_model = conn.model("current_days", result);
        const hotModel = new current_state_model({temperature: 25, humidity: 20, rain: 1, pressure:20});
        await hotModel.save();
        //console.log("success")

    }  catch (error) {
        console.log(error);
      }

    }

    run().catch(console.dir);