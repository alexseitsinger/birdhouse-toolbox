import requests
import bs4
import re
import validators
import maya
import os
import json
import uuid

DEFAULT_TIMEOUT = 10.0
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def find_urls(url, timeout=DEFAULT_TIMEOUT):
    try:
        response = requests.get(url, timeout=timeout, headers=HEADERS)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        anchors = soup.find_all("a")
        return list(set(x["href"] for x in anchors))
    except requests.ConnectionError:
        print("Connection failed: {}".format(url))
        raise []


def get_status_code(url, timeout=DEFAULT_TIMEOUT):
    try:
        response = requests.get(url, timeout=timeout, headers=HEADERS)
        return response.status_code
    except requests.ConnectionError:
        return None


def save_report(report, output_dir=None):
    if output_dir is None:
        output_dir = os.path.expanduser("~")
    output_path = os.path.join(
        output_dir, "link-report-{}.json".format(uuid.uuid4().hex)
    )
    with open(output_path, "w") as f:
        f.write(json.dumps(report))
    return output_path


def check_links(
    url,
    base_url,
    ignored_paths=[],
    output_dir=None,
    timeout=DEFAULT_TIMEOUT,
    max_links=None,
    results={},
):
    # if we don't get a base_url, assume it the url we're checking.
    if base_url is None:
        base_url = url

    # Remove duplicates, and convert it to a tupple for use in endswith.
    ignored_paths = tuple(set(ignored_paths))

    if url not in results:
        # If we reached our limit, quit early.
        if max_links is not None and len(results.keys()) == max_links:
            print("Max links limit reached.")
            return results
        # If the URL isn't valid, dont even bother trying.
        if validators.url(url) is False:
            results[url] = {
                "action_taken": "skipped",
                "reason": "invalid",
                "status_code": None,
            }
        # if the URL isn't local (to the website), then dont bother.
        elif not url.startswith(base_url):
            results[url] = {
                "action_taken": "skipped",
                "status_code": None,
                "reason": "remote",
            }
        # If the URL ends with one of the ignored paths, skip it.
        elif url.endswith(ignored_paths):
            results[url] = {
                "action_taken": "ignored",
                "status_code": None,
                "reason": "specified",
            }
        else:
            print("Checking: {}".format(url))
            results[url] = {
                "action_taken": "checked",
                "reason": "valid",
                "status_code": get_status_code(url, timeout),
            }

            # Then, repeat the process for each found url on the page.
            for found_url in find_urls(url, timeout):
                check_links(
                    found_url,
                    base_url,
                    ignored_paths,
                    output_dir,
                    timeout,
                    max_links,
                    results,
                )

    return results


def find_results(path, **kwargs):
    kw = dict(**kwargs)
    found = {"kwargs": kw, "urls": []}
    with open(path, "r") as f:
        results = json.loads(f.read())
        if "results" in results:
            results = results["results"]
        for url, result in results.items():
            if all([result[k] == v for k, v in kw.items()]):
                found["urls"].append(url)
    return found


def create_report(
    url,
    base_url=None,
    timeout=DEFAULT_TIMEOUT,
    max_links=None,
    ignored_paths=[],
    output_dir=None,
):
    started_on = maya.now()

    # If the url is unique, then try to surf it.
    results = check_links(
        url=url,
        base_url=base_url,
        ignored_paths=ignored_paths,
        output_dir=output_dir,
        timeout=timeout,
        max_links=max_links,
    )

    report = {
        "dates": {"started_on": started_on, "ended_on": maya.now()},
        "kwargs": {
            "url": url,
            "base_url": base_url,
            "timeout": timeout,
            "max_links": max_links,
            "ignored_paths": ignored_paths,
            "output_dir": output_dir,
        },
        "results": results,
    }

    # Save the results to disk.
    save_report(report, output_dir)

    # Return the results too.
    return results
