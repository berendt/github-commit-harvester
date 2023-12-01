#!/usr/bin/env python3

import calendar
import datetime
import os
import sys

from git import Repo
from loguru import logger
from pydriller import Repository
import tabulate

TABLEFMT = "github"

REPOSITORIES = {
    "osism/ansible-collection-commons",
    "osism/ansible-collection-services",
    "osism/ansible-collection-validations",
    "osism/ansible-playbooks",
    "osism/ansible-playbooks-manager",
    "osism/cfg-cookiecutter",
    "osism/cfg-generics",
    "osism/cloud-in-a-box",
    "osism/container-image-ceph-ansible",
    "osism/container-image-inventory-reconciler",
    "osism/container-image-kolla-ansible",
    "osism/container-image-osism-ansible",
    "osism/container-images",
    "osism/container-images-kolla",
    "osism/defaults",
    "osism/k8s-capi-images",
    "osism/node-image",
    "osism/openstack-flavor-manager",
    "osism/openstack-image-manager",
    "osism/openstack-project-manager",
    "osism/openstack-resource-manager",
    "osism/openstack-sandbox-manager",
    "osism/openstack-themes",
    "osism/osism.github.io",
    "osism/python-osism",
    "osism/release",
    "osism/terraform-base",
    "osism/testbed",
}

AUTHORS = ["Christian Berendt"]

YEAR = 2023
MONTH = 11

level = "INFO"
log_fmt = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | "
    "<level>{message}</level>"
)

logger.remove()
logger.add(sys.stderr, format=log_fmt, level=level, colorize=True)

num_days = calendar.monthrange(YEAR, MONTH)[1]
days = [datetime.datetime(YEAR, MONTH, day) for day in range(1, num_days + 1)]

for repository in REPOSITORIES:
    try:
        Repo.clone_from(
            f"https://github.com/{repository}.git", f"cache/{repository}"
        )
        logger.info(f"Cloning {repository}")
    except:
        r = Repo(f"repositories/{repository}")
        r.remotes.origin.pull()
        logger.info(f"Pulling {repository}")

data = []
for day in days:
    logger.info(f"Processing {day}")
    data.append([day.strftime("%Y-%m-%d"), "", ""])

    for repository in REPOSITORIES:
        commits = Repository(
            f"cache/{repository}",
            only_in_branch="main",
            since=day,
            to=day.replace(hour=23, minute=59, second=59),
            only_no_merge=True,
            only_authors=AUTHORS,
        ).traverse_commits()

        for commit in commits:
            message = commit.msg.partition("\n")[0]
            print(f"{message}, https://github.com/{repository}/commit/{commit.hash}")
            data.append(
                [
                    "",
                    commit.msg.partition("\n")[0],
                    f"https://github.com/{repository}/commit/{commit.hash}",
                ]
            )

result = tabulate.tabulate(data, headers=["Date", "Title", "URL"], tablefmt=TABLEFMT)
print(result)
