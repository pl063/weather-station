    //Define database schemas
    const mongoose = require("mongoose")
    
    const Schema = mongoose.Schema;

    //Define current_state schema
    const current_state = new Schema({
        temperature : { type: Number, default: 0 },
        humidity : { type: Number, default: 0 },
        pressure : { type: Number, default: 0 },
        rain : { type: Number, default: 0 }
      });
    
    current_state.set("timestamps", true);


      module.exports = current_state;