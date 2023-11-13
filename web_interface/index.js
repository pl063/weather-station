    const express = require("express");
    const app = express();
    const port = 5500; 
    const expressHandlebars = require("express-handlebars");

    app.engine(".hbs", expressHandlebars.create({
        extname: ".hbs",
        defaultLayout: 'main', 
        layoutsDir: __dirname + '/views/layouts/',
        partialsDir: __dirname + '/views/partials/'
    }).engine);
    app.set( "view engine" , ".hbs");
    app.use('/static', express.static('static'));
    app.use(express.urlencoded({extended: true}));
    app.set('views', './views/');

    app.enable("view cache");
    process.env.NODE_ENV === "production";

    app.route("/").get((req, res) => { res.redirect('/dashboard')
        res.statusCode = 301;
    })

    app.route("/dashboard")
    .get((req, res) => {
        res.render("homePage", {layout: "main"}, (err, html) => {
            if(err) {
                res.statusCode = 444; 
                console.log(err);
                 res.send("Something went wrong!");
                 
            } else {
                 res.send(html);
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