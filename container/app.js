const express = require('express');
const app = express();

app.get('/', (req, res) => {
  return res.status(200).json({
    status: 'success',
    message: 'running container',
  });
});

app.listen(3000, (req, res) => {
  console.log('Listening on PORT', 3000);
});
