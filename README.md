# Birdhouse Toolbox

## Description

Command line tools to automate various processes.

## Installation

```
pipx install birdhouse-toolbox
```

or

```
pipenv install birdhouse-toolbox
```

or

```
pip install birdhouse-toolbox
```

## Usage

#### Wordpress

* **create-post** 

  Adds a new post using the title and body provided, by duplicating the last published post.

  ```
  bht --url <site_url> wp create --title <title> --content <content> --slug <slug> --slug <slug> --category <category> --category <category>
  ```

* **authenticate** 

  Authenticates the username and password with the website, saves the credentials, and a JSON web token for future use. Will re-use saved credentials if none are provided.
  
  ```
  bht --url <site_url> wp auth --username <username> --password <password>
  ```


