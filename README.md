[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://opensource.org/license/mit)
[![python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![tests](https://github.com/CounterTorque/pdx-version-incrementer/actions/workflows/python-app.yml/badge.svg)](https://github.com/CounterTorque/pdx-version-incrementer/actions/workflows/python-app.yml)



# pdx-version-incrementer

A Simple tool for incrementing your Playdate PDX version number that you can hook to your builds written in python.

This standalone python file expects one parameter `-i` with a pdx file as input. 

It will read your pdx file, increment the BuildNumber by 1, then write out the file in the same location.

## Requirements


- Using PDX Files from [Playdate SDK](https://play.date/dev/) inside your own project.


## Usage

I recommend you clone this as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) inside your own project.

In the example tasks.json below, you can see that this has been cloned into a tools folder then it's source repo.

This will add a .gitmodules into your root repository. 


```json
// .vscode/tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
        "label": "(Python) Increment Build Number",
        "type": "shell",
        "command": "python",
        "args": ["${workspaceFolder}/tools/pdx-version-incrementer/source/pdx_build_increment.py", "-i", "${workspaceFolder}/source/pdxinfo"],
        "problemMatcher": [],
        "group": {
            "kind": "build"
        }
    }	
  ]
}
```

## Optional 

- Using the [PDX Debug] (https://github.com/midouest/vscode-playdate-debug) is easy to augment the `.vscode/tasks.json`. 

```json
// .vscode/tasks.json
{
    ...
    {
    "label": "Playdate: Build and Run",
    "dependsOn": ["(Python) Increment Build Number", "Playdate: Build", "Playdate: Run"],
    "dependsOrder": "sequence",
    "problemMatcher": [],
    "group": {
        "kind": "build",
        "isDefault": true
        }
    },
}
```