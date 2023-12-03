    const express = require("express");
    const logger = require("morgan");
    const mongoose = require("mongoose");
    const bodyParser = require("body-parser");
    const path = require("path");
  
    require("dotenv").config();
    const dbUrl = require("./conf.js");

    const app = express();
    const port = 5500; 
    const expressHandlebars = require("express-handlebars");

    
   
    const middleware = require("./middleware.js");
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
    app.use('/node_modules', express.static('node_modules'))
    app.use(express.urlencoded({extended: true}));
    app.use(logger("dev"));
    app.use(express.json());
    app.set('views', './views/');

    app.enable("view cache");
    process.env.NODE_ENV === "production";

    //Connect to db
    let connectedDatabase = false;
    const mongoString = dbUrl;
    //console.log(mongoString);
    mongoose.connect(mongoString);

    const database = mongoose.connection;

    database.on('error', (error) => {
        console.log(error)
    })
    
    database.once('connected', () => {
        console.log('Database Connected');
        connectedDatabase = true;
    })



    app.route("/").get((req, res) => { res.redirect('/dashboard')
        res.statusCode = 301;
    })


    app.route("/dashboard")
    .get( async function (req, res){
        try {
            //check if db is connected and use db value OR N|A
            let renderArgument = [];

            if (connectedDatabase) {
                let result = await middleware.retrieveLastEntry(database);
               // console.log(result);
                renderArgument.push(result);
            } else {
                renderArgument.push ({
                    temperature : "N/A",
                     humidity : "N/A", 
                     pressure : "N/A",
                     rain: "N/A"
                })
            }
            let {temperature, humidity, pressure, rain} = renderArgument[0];
            res.render("homePage", {layout: "main", temperature, humidity, pressure, rain}, async function (err, html){
                if(err) {
                    res.statusCode = 444; 
                    console.log(err);
                     res.send("Something went wrong!");
                     
                } else {
                     res.send(html);
                }
            });
          } catch (err) {
             console.log(err);
          }
       

        
    })

    app.route("/logs")
    .get( (req, res) => {
        res.render("homePage", {layout: "logs"}, async function(err, html) {
            if(err) {
                res.statusCode = 444; 
                console.log(err);
                 res.send("Something went wrong!");
                 
            } else {
                 res.send(html);
            }
        });
    })

    app.route("/logs/entries")
    .get( async function (req, res) {
        try {
            let entries = [];

            if (connectedDatabase) {
                let result = await middleware.retrieveEntries(database);
                console.log(result)
            } 
            res.send(entries);
        } catch (err){
            console.log(err);
        }
    })


    app.listen(port, () => console.log(`App listening on: ${port}`));