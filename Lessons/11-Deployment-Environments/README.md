<p align="center"><img style="box-shadow: none; border: none; background: none;" src="./assets/heroku.svg" height="200"></p>
<!-- .slide: class="header" -->

# Deployment Environments: Ship Early, Ship Often

➡️ [**Slides**](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/Slides/11-Deployment-Environments.html ':ignore')

<!-- > -->

### Agenda

1. [[**20m**] Quiz](#20m-quiz)
2. [[**5m**] Objectives](#5m-objectives)
3. [[**10m**] Overview: Environments](#10m-overview-environments)
4. [[**15m**] Activity: Hiding Secrets](#15m-activity-hiding-secrets)
5. [[**10m**] BREAK](#10m-break)
6. [[**25m**] Activity: Deployment Definitions](#25m-activity-deployment-definitions)
7. [[**15m**] Activity: Playlister Reflection](#15m-activity-playlistr-reflection)
8. [[**20m**] Wrap Up: Define a Deployment Plan](#20m-wrap-up-define-a-deployment-plan)
9. [Resources & Credits](#resources--credits)

<!-- > -->

## [**20m**] Quiz

<!-- > -->

## [**5m**] Objectives

**By the end of this class, you'll be able to...**

1. Identify go-to strategies to  **release** web applications.
2. Recognize and name the **environments** used during the development life cycle.
3. Protect private keys and other **secrets** using `dotenv`.
4. Create and **deploy** live Flask applications on Heroku.

<!-- > -->

<!-- .slide: data-background="#11A31B" -->

### Food for Thought

> "**_Software and cathedrals are much the same &mdash; <br> first we build them, then we pray._**"

<strong>Sam Redwine</strong>, 4th International Software Process Workshop (1988)

<!-- > -->

## [**10m**] Overview: Environments

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

# Hello to Heroku

Heroku is a turn-key server solution that serves as the **staging** and **production servers** for many, including Make School!

It combines web hosting functionality with a rich marketplace of plugins to extend and enhance your server --- like an app store for your web application!

<!-- v -->

## [**25m**] Activity: Deployment Definitions


<div class="compact">

Using the [Glossary of Heroku Terminology](https://devcenter.heroku.com/articles/glossary-of-heroku-terminology), use your own words to define the following terms:


1. App
2. Add-On
3. Config Var
4. Dyno
5. Process Type
6. Procfile
7. Release


Discuss, then spend about 15 minutes writing **one** short sentence for each term.

</div>

<!-- v -->

### [**10m**] Review Definitions

<!-- v -->

## [**15m**] Activity: Playlistr Reflection

**Write down any issues you had while deploying Playlistr.**

* What broke?
* What didn't make sense?
* Did anyone around you face the same issues?

After a few minutes, we'll talk about the challenges you encountered!

<!-- > -->

## [**20m**] Wrap Up: Define a Deployment Plan

1. Consider the features you'll be developing for your contractor project.
2. Write down three opportunities to push to staging during your development cycle.
3. Review these potential deployments with someone you haven't worked with yet!

<!-- > -->

## Resources & Credits

- [Difference Between Development, Stage, And Production](https://dev.to/flippedcoding/difference-between-development-stage-and-production-d0p)
- [Deploying Python Applications with Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn)
- [Heroku Tips and Hacks](https://www.airpair.com/heroku/posts/heroku-tips-and-hacks)
- [Glossary of Heroku Terminology](https://devcenter.heroku.com/articles/glossary-of-heroku-terminology)
- [The Procfile](https://devcenter.heroku.com/articles/procfile)
