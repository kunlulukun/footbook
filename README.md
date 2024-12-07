# What's this
SNS web application developed for learning


# How to run
```sh
# to run everything in this project
docker compose up

# to run specific component of the project with necessary dependency
docker compose up api-server
docker compose up frontend
```



# How to contribute
**ATTENTION: Please do not directly push any branch or commit to this repo.**

1. fork this repo
2. create branch in your own repo and make commit there
3. create pull request for merging changes to this repo.

Tips: 
```bash
git clone git@github.com:your_account/footbook.git

cd ./footbook

git remote add upstream git@github.com:kunlulukun/footbook.git
git remote set-url --push upstream NO-PUSH


# To keep update with latest master branch
git fetch --all
git checkout master
git merge upstream/master
```
