// routes/secure.js

const express = require('express');
const router = express.Router();
const requireApiKey = require('../middleware/requireApiKey');

router.post('/data', requireApiKey, (req, res) => {
  res.json({
    message: "Secure data received successfully",
    body: req.body
  });
});

module.exports = router;
