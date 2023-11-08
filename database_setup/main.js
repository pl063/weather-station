//Setup Mongo database with Node JS
    import mongoose from "mongoose";

    import * as conf from "./conf.js";
    import * as schemas from "./schemas.js";

    const username = encodeURIComponent(conf.USER.username);
    const password = encodeURIComponent(conf.USER.password);
    let uri =
    `mongodb+srv://${username}:${password}@weather-station.lllcyel.mongodb.net/?retryWrites=true&w=majority`;

    async function run() {

    try {
        const conn = await mongoose.createConnection(uri);
        console.log("Connected to db");
        const current_state_model = conn.model("current_state", schemas.current_state);
        const testModel = new current_state_model({temperature: 25});
        await testModel.save();
        console.log("success")

    }  catch (error) {
        console.log(error);
      }

    }

    run().catch(console.dir);