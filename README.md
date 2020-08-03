# smoothies

!! Make sure to change the secret keys in `/smoothies/api-server/config.py` preferably by setting environment variable `export SECRET_KEY=<somethingSecure>` 

Simple web app that uses Vue as front-end to fetch data from Flask RESTFull API backend

## Back end

### Create environment variables
export FLASK_APP=app

### Setup virtual environment
python3 -m venv venv

### Activate virtual environment
. ./venv/bin/activate

### Install dependencies
pip install -r requirements

### Run API server
cd into `api-server`
use command `flask run`

> A Vue.js project

## Vue Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
