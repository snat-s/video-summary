const fs = require('fs');
const path = require('path');
const express = require("express");
const childProcess = require('child_process');

const app = express();

// Middleware
app.use(express.static('public'));
app.use(express.json());
app.use((req, res, next) => {
    // CHANGE this headers for whatever you actually want.
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get("/", (req, res) => {
    res.json({message: "This is the base of the api m8"});
});

app.post("/", async (req, res) =>  {
    const { link } = req.body;
    console.log(link);

    //const link = "https://www.youtube.com/watch?v=jKXDUBqdrxE";
    try {
        const result = await childProcess.exec(`yt-dlp -x ${link}`, (err, stdout, stderr) => {
            if (err) throw err;

            const regex = /Destination: (.+)\.opus/g;
            const result = regex.exec(stdout);
            let opusFileName = result[0].replace("Destination: ","");

            console.log("Finished downloading the video");
            childProcess.exec(`python ../python_pipeline/summarize_youtube.py '${opusFileName}'`, (err, stdout, stderr) => {
                if (err) throw err;
                console.log(stdout);
                stdout = stdout.replace("TRANSCRIPTION", "<h2>Transcription:</h2><br>\n");
                stdout = stdout.replace(/Detected language: \w+\s/, "");
                //stdout = stdout.replace("[]", "")
                res.status(200).json({message: "<br><h2>TLDR:</h2><br>"+stdout});
            });
        });
    } catch (err) {
        console.err(err);
        res.status(500).json({message: "there has been an error"})
    }
});

app.listen(8888, () => {
    console.log("Server listening on port 8888");
});
