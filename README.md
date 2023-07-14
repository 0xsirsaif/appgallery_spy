# AppGallerySpy

`appgalleryspy` is a powerful tool designed to download app reviews from Huawei's AppGallery. It utilizes Selenium to crawl the Huawei website and retrieve user reviews. This tool is built as a command-line interface (CLI) using Typer, making it easy to use and integrate into your workflows.

## Deliverables

- [x] Developed a CLI application using `Typer`, facilitating easy downloading of app reviews from Huawei's AppGallery
- [x] Utilized semantic commit messages to maintain a clear and descriptive commit history.
- [x] Successfully understood the structure and behavior of Huawei's AppGallery site and implemented effective crawling strategies to retrieve app reviews.
- [x] Dockerized the project, enabling easy testing of the application in a containerized environment using docker-compose.
- [x] Implemented a FastAPI application to serve as an api to retrieve app recent reviews.
- [x] Implemented a `--limit` option to limit the number of reviews to be downloaded.
- [x] Utilized `pytest` and `pytest-cov` for running tests and generating coverage reports to assess the test coverage of the codebase.
- [x] Incorporated `pre-commit` hooks to ensure consistent formatting, type checking, and linting before each commit.
- [x] Automated formatting and versioning of the package using a `Makefile`.
- [x] Published the package on PyPI at https://pypi.org/project/appgallery_spy/
- [x] Documentation including installation instructions, usage guidelines, known issues, and testing instructions.

## Installation

### Inside a Docker Container

- the web service is available at http://localhost:8004
- the api documentation is available at http://localhost:8004/docs

1. Run `docker-compose up --build` to build the image and run the container
2. Run `docker-compose exec web bash` to enter the container
3. The `appgallery_spy` CLI is now available inside the container
4. Or run `python -m appgallery_spy` inside the container too

### Published CLI

1. Install the package using `pip install appgallery_spy`
2. Run `appgallery_spy --help` to see the available commands and options

```bash
Usage: python -m appgallery_spy.cli [OPTIONS] APP_ID                                                                                                                                            
                                                                                                                                                                                                 
╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    app_id      TEXT  [default: None] [required]                                                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --limit                     INTEGER                          [default: 3]                                                                                                                     │                                                                      │
│ --help                                                       Show this message and exit.                                                                                                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Manually

1. Clone the repository, `git clone git@github.com:0xsirsaif/appgallery_spy.git`, and `cd` into it
2. Create a virtual environment, `python -m venv venv`, and activate it, `source venv/bin/activate`
3. Install the dependencies, `pip install -r requirements.txt`
4. Run `python -m appgallery_spy --help` to see the available commands and options

## Usage

- Run `python -m appgallery_spy [APP_ID]` to download reviews for the app with the given `APP_ID`
- Run `python -m appgallery_spy [APP_ID]` with the `--limit` option to limit the number of scrolls to be performed

## Testing

- To run all tests, run the following command:
```bash
$ python -m pytest --cov tests/ -vvs
```

## Known Issues

- Inserting data after crawling: The MongoDB client raises a ServerSelectionTimeoutError, preventing successful data insertion. Work is in progress to fix this issue and will be resolved soon. Apologies for any inconvenience caused.