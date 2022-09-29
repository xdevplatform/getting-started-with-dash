# Getting Started with Dash

Let’s say you want to create a webpage where you can visualize how often you are Tweeting. For example, you could use the recent Tweets counts endpoint and Dash to create a website that automatically refreshes to show how much you are Tweeting throughout the week. The code sample in this repository corresponds to [this tutorial](https://developer.twitter.com/en/docs/tutorials/getting-started-dash). This sample is currently deployed on [Glitch](https://getting-started-dash.glitch.me/).

## Remixing
- Vist the [Glitch project](https://glitch.com/~getting-started-dash) and click where it says "Remix".
- A developer account.
  - If you don’t already have access to the Twitter API, [you can sign up for a developer account.](http://t.co/signup)
- A Project in the [developer portal](https://developer.twitter.com/en/portal/dashboard)
- An App containing the credentials required to use the Twitter API. You will be using bearer token authentication for this sample.
- Update your `.env` file to include your bearer token `BEARER_TOKEN=your-bearer-token`
- Update the query to include your own handle 
```python
{"query": "from:jessicagarson", "granularity": "day"}
```


