# Using this Repository

This repository is meant to be used with the [Copier](https://copier.readthedocs.io/en/stable/) utility to create a boilerplate web-based experiment running with [jsPsych](https://www.jspsych.org/latest/) against [AutoRA](https://github.com/autoresearch/autora/).

Detailed instructions for how to use Copier with this repository can be found [here](docs%2Fcopier.md).

Details of the Copier questionnaire are described [here](docs/questionnaire.md).

#### Copier will generate some configuration files along with the web application.

A `Dockerfile` can, optionally, be created so that the web application can be deployed as a container if the target server supports containers.

GitHub Actions `yaml` files can, optionally, be created for automating deployment from a GitHub repository, should you choose to commit the web application Copier creates. These will be in the `.github/workflows` subdirectory and may be "hidden" in your system user interface. They should be visible from the shell/terminal.

Even if your target server does not come with Docker installed, if you would like to try Docker locally we have compiled some instructions for getting started [here](docs%2Fdocker.md). One of the GitHub Actions yaml files supports deploying using the `Dockerfile`. The advantage here is that how the web application functions in your local instance of Docker will be a faithful representation of how it will function on the deployment server.