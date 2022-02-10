# Javascript (Node)

To use this helper script, add the [New Relic Nodejs agent](https://docs.newrelic.com/docs/apm/agents/nodejs-agent/installation-configuration/install-nodejs-agent/) and add the script found in this directory to your project.

## Express example:

```js
const express = require('express');

// Add the New Relic APM agent.
const newrelic = require('newrelic');

// Add the helper script.
// Feel free to place this wherever make sense for your application.
const getCustomAttributes = require('./getCustomAttributes.js');

const app = express();

// ...

app.post(/"move", (req, res) => {
  newrelic.addCustomAttributes(getCustomAttributes(req.body));
  // ...your snake logic goes here
});
```
