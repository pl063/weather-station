    const express = require("express");
    const app = express();
    const port = 5500; 
    const expressHandlebars = require("express-handlebars");

    app.engine(".hbs", expressHandlebars.create({
        extname: ".hbs"
    }).engine);
    app.set( "view engine" , ".hbs");
    app.use('/static', express.static('static'));
    app.use(express.urlencoded({extended: true}));
    app.set('views', './views/');

    app.route("/").get((req, res) => { res.redirect('/dashboard')
        res.statusCode = 301;
    })

    app.route("/dashboard")
    .get((req, res) => {
       res.render("homePage", (err, html) => {
           if(err) {
               res.statusCode = 444; 
               console.log(err);
                res.send("Something went wrong!");
                
           } else {
                res.send(html);
           }
       })
    })


    app.listen(port, () => console.log(`App listening on: ${port}`));