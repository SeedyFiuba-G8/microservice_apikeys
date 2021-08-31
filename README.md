# [API Keys Microservice](https://seedyfiuba-g8.github.io/)

Written in Python (FastAPI).

Visit our project page [_here_](https://seedyfiuba-g8.github.io/).

## DISCLAIMER: ¡Currently offline! :broken_heart:

Since we used **Heroku** to host our microservices, as they offer a limited number of free applications, we decided to remove them. CI/CD has been manually disabled.

If you were to deploy this application, you should:

-   Manually enable the workflow from GitHub Actions.
-   Create your Heroku app to host our `main` (and optionally `dev` branch). Keep in mind this Heroku app should have the following `ENV_VARS`:
    -   `FASTAPI_ENV`: `main`, `dev`.
-   Setup **secrets** needed by our workflow (mainly Heroku credentials and application name).
-   **Happy coding!**
