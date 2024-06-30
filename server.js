const express = require('express');
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'Front-End')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'Front-End', 'index.html'));
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});