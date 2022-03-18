# Python

To use this helper script, add the [New Relic Python agent](https://docs.newrelic.com/docs/apm/agents/python-agent/getting-started/introduction-new-relic-python/) and add the script found in this directory to your project.

## Flask example:

```python
from flask import Flask

# Add the New Relic APM agent.
import newrelic

# Add the helper script.
# Feel free to place this wherever makes sense for your application.
from getCustomAttributes import getCustomAttributes

app = Flask(__name__)

# ...

@app.post("/move")
def handle_move():
    data = request.get_json()
    attributes = getCustomAttributes(data)
    for key, value in attributes.items():
        newrelic.agent.add_custom_parameter(key, value)
    # ...your snake logic goes here

@app.post("/end")
def handle_end():
    data = request.get_json()
    attributes = getCustomAttributesEnd(data)
    for key, value in attributes.items():
        newrelic.agent.add_custom_parameter(key, value)
    # ...other logic here
```
