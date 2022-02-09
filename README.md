# Battlesnake Custom Attributes for New Relic

In this repository you can find code and instructions for instrumenting a Battlsnake's performance with [New Relic custom attributes](https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/collect-custom-attributes/). If you would like to add instrumentation in a language that is not yet documented in this repository, please use to following format for consistency (and consider submitting a PR!).

## Custom Attribute Format

Use the following JSON format for adding your custom attributes. These will appear alongside the relevant _Transaction_ data in New Relic.

This example uses the POST request from the [Battlesnake API docs](https://docs.battlesnake.com/references/api/sample-move-request):

```json
{
  "snakeGameId": 'game-00fe20da-94ad-11ea-bb37',
  "snakeRules": 'standard',
  "snakeTurn": 14,

  "snakeBoardHeight": 11,
  "snakeBoardWidth": 11,
  "snakeBoardFood": 'W3sieCI6NSwieSI6NX0seyJ4Ijo5LCJ5IjowfSx7IngiOjIsInkiOjZ9XQ==',
  "snakeBoardHazards": W3sieCI6MywieSI6Mn1d,

  "snakeName": 'My Snake',
  "snakeId": 'snake-508e96ac-94ad-11ea-bb37',
  "snakeHealth": 54,
  "snakeLength": 3,
  "snakeData": 'eyJib2R5IjpbeyJ4IjowLCJ5IjowfSx7IngiOjEsInkiOjB9LHsieCI6MiwieSI6MH1dLCJoZWFkIjp7IngiOjAsInkiOjB9LCJjb2xvciI6IiNGRjAwMDAifQ==',

  "snakeOpponent_1_Name": 'Another Snake',
  "snakeOpponent_1_Id": 'snake-b67f4906-94ae-11ea-bb37',
  "snakeOpponent_1_Health": 16,
  "snakeOpponent_1_Length": 4,
  "snakeOpponent_1_Data": 'eyJib2R5IjpbeyJ4Ijo1LCJ5Ijo0fSx7IngiOjUsInkiOjN9LHsieCI6NiwieSI6M30seyJ4Ijo2LCJ5IjoyfV0sImhlYWQiOnsieCI6NSwieSI6NH0sImNvbG9yIjoiIzI2Q0YwNCJ9'
}
```

In order to keep keep the attribute size under the [255 byte limit](https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/data-requirements-limits-custom-event-data/), some of the board state should be turned into a JSON string and base64 encoded:

| Attribute              | Description                                                                    |
| ---------------------- | ------------------------------------------------------------------------------ |
| `snakeBoardFood`       | `board.food` in the POST request                                               |
| `snakeBoardHazards`    | `board.hazards` in the POST request                                            |
| `snakeData`            | The `body`, `head` and `customizations.color` (as `color`) data for your snake |
| `snakeOpponent_N_Data` | Same as `snakeData` for each opponent                                          |

These encoded values are optional, but will be utilized for some upcoming custom visualizations in New Relic.
