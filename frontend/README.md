# Frontend
This is the frontend code of the app.


## Project Setup

if you don't have node environment

```sh
brew install nvm

nvm use lts/iron 

```
### Install dependencies
```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```


## Run with nginx in docker

### Option 1. use dockerfile to build a image

```sh
docker build -t frontend .

docker run -p 3000:80 frontend
```

You can access to the webpage on localhost:3000


### Option 2. docker compose up

TBD