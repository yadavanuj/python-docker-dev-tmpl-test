# A Python Docker Development Template

> This is a work in progress. Kindly post issues and contribute to make it better. Apologies in advance.

## Usage

1. Clone the repository in the folder of your choice or you can copy-paste the content
2. Create a folder name `db` in the `root` directory.
3. Create a new file named `password.txt` in the `db` directory.
4. Add your database or some password (e.g. `mysecurepassword`) in the `password.txt` file.

## VSCode

1. Install Python Extension

![VSCode Python Extension](https://github.com/yadavanuj/bondAI-docker-dev-tmpl/blob/main/static/vscode-ext.png?raw=true)

2. Create Gemini Key
   [Google AI Studio](https://aistudio.google.com/app/apikey)

3. Create environment file

> Name: env.txt, must be placed next to main.py with below content

![ENV](https://github.com/yadavanuj/bondAI-docker-dev-tmpl/blob/main/static/env.png?raw=true)

> This file has been ignored in .gitignore

## To build and run application

```
docker compose up --build
```

Your application will be available at http://localhost:8000.

## To Run and Watch (Live Reload)

```
docker compose watch
```

## Verify

1. Install VS Code Extension : Thunder Client

### Create - POST

![Create Post](https://github.com/yadavanuj/bondAI-docker-dev-tmpl/blob/main/static/post.png?raw=true)

### Get ALL

![Get All Posts](https://github.com/yadavanuj/bondAI-docker-dev-tmpl/blob/main/static/posts.png?raw=true)

## Bond AI, Ask API

The new api integrates basic Google Gemini AI Bot. You can already start asking interesting questions like:

![Ask API](https://github.com/yadavanuj/bondAI-docker-dev-tmpl/blob/main/static/ask.png?raw=true)
