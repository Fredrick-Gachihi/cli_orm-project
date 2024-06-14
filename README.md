## Cli project
Date: 2024/6/11

By Fredrick Gachihi Mwaura.

## Introduction
This project is a command-line interface (CLI) tool designed for managing real shop data.  

## Key Features
Database Management: Initialize and maintain a SQLite database (shop.db) that stores information about the items.


<!-- 
## Layout
└── lib 
├── models │ 
├── __init__.py │ 
└── model_1.py 
├── cli.py 
├── config.py 
├── debug.py 
└── helpers.py  -->

## Installation and Usage
Installation: Clone the repository, install dependencies using Pipenv, and initialize the database.
Usage: Utilize the CLI commands provided (addagent, addproperty, addclient, viewproperties, viewclients) to manage agents, properties, and clients efficiently from the command line.
## Commands
Add agent: pipenv run python lib/cli.py addagent
Add property: pipenv run python lib/cli.py addagent
Add client: pipenv run python lib/cli.py addclient
View properties: pipenv run python lib/cli.py viewproperties
View clients: pipenv run python lib/cli.py viewclients

## Purpose
This tool simplifies real estate management tasks by providing a streamlined interface to handle agent details, property listings, client registrations, and data retrieval, all within a SQLite database environment. 

## Technologies used
-Python
-Sql-lite


© 2024 Fredrick Gachihi Mwaura