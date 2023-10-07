const express = require('express');
const bodyParser = require('body-parser');
const puppeteer = require('puppeteer');
const crypto = require('crypto');
const fs = require('fs');

const secret_endpoint = crypto.randomBytes(32).toString('hex');

const port = 1337;

const app = express();

const flag = fs.readFileSync('flag.txt', 'utf8');

app.use(bodyParser.urlencoded({extended: false}));
app.set('view engine', 'ejs');

app.get('/', async function(req, res) {
    const id = Math.floor(Math.random() * 800);
    res.render('index', {id});
});

// endpoint for only admin to access your name idea (finding this is not the challenge)
app.get('/'+secret_endpoint, function(req, res) {
    const message = req.query.message ?? "";
    const id = req.query.id ?? "";

    res.render('view', {message, flag, id});
});

// endpoint for you to submit your flag to the admin
app.get('/submit', async (req, res) => {
    // check if the request is from the bot (prevent infinite looping)
    if (req.headers["is-bot"]) {
        return res.render("view", {message: 'hey!', flag: '', id: 1});
    }
    
    // get parameters from the the form you submitted
    const message = req.query['pokemon-name'] ?? "";
    const id = req.query['pokemon-id'] ?? "";

    // simulate the admin opening your name idea
    const browser = await puppeteer.launch({args: ['--no-sandbox']});
    const page = await browser.newPage();

    await page.setExtraHTTPHeaders({'is-bot': 'true'});

    await page.setDefaultNavigationTimeout(3000);

    await page.setBypassCSP(true);

    try {
        const a = await page.goto(`http://localhost:${port}/${secret_endpoint}?id=${id}&message=${encodeURIComponent(message)}`, {
            waitUntil: 'networkidle0'
        });
        await page.waitForDelay(1500);
    } catch(e) {
        // console.error(e);
    } finally {
        await page.close();
        await browser.close();
    }

    // send you back your own name idea so you can preview what the admin saw
    res.render('view', {message, flag: 'ur not admin lol', id});
});

app.listen(port, function() {
    console.log("Listening on port " + port);
});
