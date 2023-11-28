    //Define database schemas
    import mongoose from "mongoose";
    
    const Schema = mongoose.Schema;

    //Define current_state schema
    const current_state = new Schema({
        temperature : { type: Number, default: 0 },
        humidity : { type: Number, default: 0 },
        pressure : { type: Number, default: 0 },
        rain : { type: Boolean, default: false },
        time : { type: Date, default: Date.now}
      });
    

      export {current_state}