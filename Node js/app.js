const express = require('express');
const app = express();
const secureRoutes = require('./routes/secure');

app.use(express.json());

app.use('/secure', secureRoutes);

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
