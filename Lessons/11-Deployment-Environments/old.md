<!-- > -->

## [**30m**] Activity: Going Live - Gif Search

Run all commands in the root of your repository.

<!-- v -->

Install `gunicorn`:

```bash
pip install gunicorn
```

<!-- v -->

1. Create a file named `Procfile` that contains the following:

```bash
web: gunicorn app:app
```

<!-- v -->

1. Execute `heroku create <<PROJECT NAME>>` to create an instance of your Gif Search project on Heroku.

PROTIP: Run `heroku apps` to see all your Heroku applications.

<!-- v -->

1. Run `heroku open` to open your project.

_(It shouldn't work --- yet!)_

<!-- v -->

1. Run `heroku logs --tail` and read the logs to see why your deployment didn't go as planned.

- What error did you receive?
- **HINT**: Run `heroku config`. What do you think could be missing?

<!-- v -->

1. **We haven't told Heroku about our `dotenv` settings**! Run the following commands to populate your `.env` variables in your current Heroku instance:

 ```bash
 $ heroku config:set FLASK_APP=app.py
 Setting FLASK_APP and restarting flask-gifsearch... done, v2

 $ heroku config:set TENOR_API_KEY=yourapikeyvalue
 Setting TENOR_API_KEY and restarting flask-gifsearch... done, v3
 ```

<!-- v -->

1. Run `heroku open` one more time, and ensure the above commands fixed the bug found in the logs.

<!-- v -->

1. **Celebrate** your very first push to production! **Paste your link in the course Slack channel**.
