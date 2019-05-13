# Birdhouse Toolbox

## Description

Command line tools automate various online marketing processes.

## Installation

```
pip install birdhouse_toolbox
```

## Usage

#### Wordpress

* __get-post__: Returns the post as JSON.
  ```
  bht --url <site_url> wordpress get-post --id <post_id>
  ```
* __get-posts__: Reurns a list of posts as JSON.
  ```
  bht --url <site_url> wordpress get-posts
  ```
* __add-post__: Adds a new post using the title and body provided, by duplicating the last published post.
  ```
  bht --url <site_url> wordpress add-post --title <title> --markup <markup>
  ```
* __authenticate__: Authenticates the username and password with the website, saves the credentials, and a JSON web token for future use. Will re-use saved credentials if none are provided.
  ```
  bht --url <site_url> wordpress authenticate (--username <username> --password <password>)
  ```

#### Analytics

* __get-report__: Returns the report data for the specified date range.
  ```
  bht --url <site_url> analytics get-report --start <start_date> --end <end_date> (--template <path_to_template> --output <path_for_output_pdf>)
  ```
* __authenticate__: Authenticates the username and password with the website, saves the credentials, and a JSON web token for future use. Will re-use saved credentials if none are provided.
  ```
  bht --url <site_url> analytics authenticate (--username <username> --password <password>)
  ```

