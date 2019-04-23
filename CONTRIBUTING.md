# Contributing guidelines

Thank you for taking the time to contribute! :tada:

## What should I know before I get started?

Please make sure to read our [READ_ME](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/README.md) in order to get to know more about our project, system requirements and how to build the system.

Make sure to read our [Code of conduct](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/CODE_OF_CONDUCT.md) as well.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please refer to the list of open issues, someone may have already reported it.
When creating a bug report, please provide as much information as possible:

* Your title should be clear and descriptive
* Describe the steps to reproduce the bug
* Tell us what was expected and what happened that didn't go as such
* Include any images or screenshots that could help to identify the problem
* If the problem isn't related to any specific action, explain what you were doing at the time it happened
* Say which OS you are using
* Say which version of the system you encountered this bug

### Suggesting Enhancements

Before suggesting an enhancement, please refer to the list of open issues, someone may have already suggested it.
When suggesting an enhancement, please provide as much information as possible:

* Your title should be clear and descriptive
* Describe how the enhancement would work step by step and how it would take place
* Provide examples
* Include any images or screenshots that could help elucidate the enhancement
* Explain why the enhancement would be useful
* Say which OS you are using
* Say which version of the system you encountered this bug

### How do I run Ada?

#### Running Ada on Telegram

To run Ada using Telegram, follow these instructions:

* Install ngrok following the instructions on [link](https://ngrok.com/download).

* Open a terminal and run ngrok on port 5001:

```sh
./ngrok http 5001
```

* Export enviroment variables:

```sh
- export ACCESS_TOKEN='TELEGRAM_ACCESS_TOKEN'
- export BOT_NAME='BOT_NAME'
- export WEBHOOK_URL='WEBHOOK_URL'
```

Install Docker based on the instructions given on the links:

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/#install-compose)

How to run Docker:

* Run this command to start the container on your computer:

```sh
docker-compose -f docker-compose-dev.yml up --build
```

#### Running Ada on a Terminal

To run Ada locally on a Terminal, install Docker based on the instructions given on the links:

* [docker](https://docs.docker.com/install/)
* [docker-compose](https://docs.docker.com/compose/install/#install-compose)

Then follow these commands:

* Run the following command to create the image of the container:

```sh
docker-compose -f docker-compose-dev.yml up --build
```

* Run Docker:

```sh
docker exec -it container_id bash
```

* Run the following commands to train Ada:

```sh
python3 -m rasa_core.run -d models/dialogue -u models/nlu/current --debug --endpoints endpoints.yml
```

Afterwards you can chat with Ada and see the logs from Rasa.


## Templates

In order to make any contribution, please refer to our templates:

* [Issue template](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/.github/ISSUE_TEMPLATE/issue-template.md)
* [Pull request template](https://github.com/fga-eps-mds/2019.1-ADA/blob/master/pull_request_template.md)
* [Template for commits](https://github.com/fga-eps-mds/2019.1-ADA/)
