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

![VSCode Python Extension](https://github.com/yadavanuj/bondAI-docker-dev-tmpl/blob/main/static/post.png?raw=true)

### Get ALL

![VSCode Python Extension](https://github.com/yadavanuj/bondAI-docker-dev-tmpl/blob/main/static/posts.png?raw=true)
