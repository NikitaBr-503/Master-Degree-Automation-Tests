API_HOSTS = {
    "test": "http://masterdegreewebapp.local/",
    "dev": "",
    "prod": ""
}

WOO_API_HOSTS = {
    "test": "http://masterdegreewebapp.local/",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
        "test": {
            "host": "127.0.0.1",
            "database": "wp398",
            "table_prefix": "wp2p_",
            "socket": " ",
            "port": 8889
        },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
    },
    'docker': {
        "test": {
            "host": "host.docker.internal",
            "database": "wp398",
            "table_prefix": "wp2p_",
            "socket": None,
            "port": 3306
        },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
    },
}