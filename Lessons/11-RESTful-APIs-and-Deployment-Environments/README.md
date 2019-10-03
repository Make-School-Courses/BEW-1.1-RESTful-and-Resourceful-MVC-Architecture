<p align="center"><img style="box-shadow: none; border: none; background: none;" src="./assets/heroku.svg" height="200"></p>

# Ship Early, Ship Often

### Some Good Tagline

➡️ [**Slides**](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/Slides/11-RESTful-APIs-and-Deployment-Environments.html ':ignore')

<!-- > -->

### Agenda

1. [[**20m**] Quiz](#20m-quiz)
2. [[**5m**] Objectives](#5m-objectives)
3. [[**10m**] Overview: Environments](#10m-overview-environments)
4. [[**15m**] Activity: Hiding Secrets](#15m-activity-hiding-secrets)
5. [[**10m**] BREAK](#10m-break)
6. [[**15m**] TT: Heroku](#15m-tt-heroku)
7. [[**30m**] Activity: Going Live - Gif Search](#30m-activity-going-live---gif-search)
8. [Resources & Credits](#resources--credits)

<!-- > -->

## [**20m**] Quiz

<!-- > -->

## [**5m**] Objectives

**By the end of this class, you'll be able to...**

1. Identify go-to strategies to  **release** web applications.
2. Recognize and name the **environments** used during the development life cycle.
3. Protect private keys and other **secrets** using `dotenv`.
4. Create and **deploy** live Flask applications on Heroku.
5. Send a friend or family member a link to a **working website**!

<!-- v -->

### `TODO` Why Should I Learn This?

<!-- > -->

<!-- .slide: data-background="#11A31B" -->

### Food for Thought

> "**_Software and cathedrals are much the same &mdash; <br> first we build them, then we pray._**"

<strong>Sam Redwine</strong>, 4th International Software Process Workshop (1988)

<!-- > -->

## [**10m**] Overview: Environments

`TODO`: Add image of environments and code workflow here.

<!-- v -->

### 1️⃣ Development

- On your computer, otherwise known as _**"locally"**_.
- Where **ALL** code updates occur.
- Connects to a database on your computer.
- Run your **tests** here before pushing your code.
- **Changes will not affect the live website**.
- **EXAMPLE**: `http://localhost:5000`

<!-- v -->

### 2️⃣ Test / Staging

- All of the **code now lives on a server**.
- As similar to production as possible.
- **EXAMPLE**: `https://projectname-test.herokuapp.com`

<!-- v -->

### 3️⃣ Production

- **Highest priority** environment.
- Where we "**go live**", "**launch**", or "**ship**" our website.
- Real live **people will find bugs** you missed while coding!
- **EXAMPLE**: `https://www.projectname.com`

<!-- v -->

### Minor Differences Allowed

Environments *can* vary, but *should* be as **similar as possible**.

**Acceptable differences** include:

- **Environment variables** and other **configuration settings**.
- Different **data** in your local database versus production.
- Static **assets** in staging and production (`.css`, `.js`) are typically minified into a single, large file.

<!-- v -->

### Public Service Announcement

<p align="center"><img style="box-shadow: none; border: none; background: none;" src="./assets/worksonmymachine.jpg" height="300"></p>

When an **unhandled exception** occurs in your application, **your website will go offline**. This is known as **downtime**.

Even **minor differences** can cause these kinds of  **unanticipated failures in production** --- _even if it worked perfectly in development!_

<!-- v -->

### Environment Variables

Sometimes you can't save everything into your code files because that would be insecure. For example, if you use a third party service like Amazon Web Services (AWS), then there will be sensitive keys that if you expose to the world on a public Github repo, hackers will steal them and use your codes to rack up hundreds of dollars in fees.

To secure such data, developers use **environment variables**,stored locally and in production.

<!-- > -->

## [**15m**] Activity: Hiding Secrets

### Protect Your Tenor API Key

<!-- v -->

### Step One

Add the `python-dotenv` package to your Gif Search project:

```bash
$ pip3 install python-dotenv
```

<!-- v -->

### Step Two

Add a `.env` file with the following **key-value pair**:

 ```bash
 TENOR_API_KEY=yourapikeyvalue
 ```

- Keys and their values are separated by `=`
- **PROTIP**: Don't use quotes in this file!

<!-- v -->


### Step Three

Add the following code **at the very top** of your `app.py` file:

 ```py
 import os

 from dotenv import load_dotenv
 load_dotenv()
 ```

This code **imports** the `python-dotenv` library and **loads all the settings** in your `.env` file!

<!-- v -->

### Step Four

Grab any setting you defined in the `.env` file via `os.getenv()`:

```py
  import os

  from dotenv import load_dotenv
  load_dotenv()

  TENOR_API_KEY = os.getenv("TENOR_API_KEY")
```

<!-- > -->

## [**10m**] BREAK

<!-- > -->

## [**15m**] TT: Heroku

Heroku will be the host we use for our production environment. Heroku is a turn-key server solution that provides a rich marketplace of plugins to extend and enhance your server:

`TODO`: List of Heroku features

<!-- > -->

## [**30m**] Activity: Going Live - Gif Search

<!-- v -->

1. Execute `heroku create <<PROJECT NAME>>` to create a heroku project for your Gif Search app.

<!-- v -->

1. Push your code to heroku and run `heroku open` to open your project.

_(It shouldn't work --- yet!)_

<!-- v -->

1. Run `heroku logs --tail` and read the logs to see why your deployment didn't go as planned.

- What error did you receive? What do you think could be missing?
- **We haven't told Heroku about our `dotenv` settings**!

<!-- v -->

1. Run the following commands to populate your `.env` variables in your current Heroku instance:

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

<!-- > -->

## Resources & Credits

- [Difference Between Development, Stage, And Production](https://dev.to/flippedcoding/difference-between-development-stage-and-production-d0p)
