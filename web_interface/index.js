    const express = require("express");
    const logger = require("morgan");
    const mongoose = require("mongoose");
    const bodyParser = require("body-parser");
  
    require("dotenv").config();

    const app = express();
    const port = 5500; 
    const expressHandlebars = require("express-handlebars");

    
    const dataScheme = require("../database_setup/schemas.cjs");
  //  const getCurrentState = require("./fetchDb.js")

    app.engine(".hbs", expressHandlebars.create({
        extname: ".hbs",
        defaultLayout: 'main', 
        layoutsDir: __dirname + '/views/layouts/',
        partialsDir: __dirname + '/views/partials/'
    }).engine);

   app.use(bodyParser.json({limit: "50mb"}));
    app.use(bodyParser.urlencoded({limit: "50mb", extended: true, parameterLimit:50000}));

    app.set( "view engine" , ".hbs");
    app.use('/static', express.static('static'));
    app.use(express.urlencoded({extended: true}));
    app.use(logger("dev"));
    app.use(express.json());
    app.set('views', './views/');

    app.enable("view cache");
    process.env.NODE_ENV === "production";

    //Connect to db
    const mongoString = process.env.DATABASE_URL;
    mongoose.connect(mongoString);

    const database = mongoose.connection;

    database.on('error', (error) => {
        console.log(error)
    })
    
    database.once('connected', () => {
        console.log('Database Connected');
    })



    app.route("/").get((req, res) => { res.redirect('/dashboard')
        res.statusCode = 301;
    })


    app.route("/dashboard")
    .get( function (req, res){
        res.render("homePage", {layout: "main"}, async function (err, html){
            if(err) {
                res.statusCode = 444; 
                console.log(err);
                 res.send("Something went wrong!");
                 
            } else {
                 res.send(html);
                 //retrieve current state
                    try {
                      
                      const res = await database.model("current_days",dataScheme).findOne().sort('-created_at').exec();
                      //todo send header with info for the last state
                    } catch (err) {
                       console.log(err)
                    }
                
            }
        });

        
    })

    app.route("/logs")
    .get( (req, res) => {
        res.render("homePage", {layout: "logs"}, (err, html) => {
            if(err) {
                res.statusCode = 444; 
                console.log(err);
                 res.send("Something went wrong!");
                 
            } else {
                 res.send(html);
            }
        });
    })


    app.listen(port, () => console.log(`App listening on: ${port}`));