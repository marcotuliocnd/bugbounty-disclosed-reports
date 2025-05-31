# Leaking sensitive information through JSON  file path.

## Report Details
- **Report ID**: 1211061
- **URL**: https://hackerone.com/reports/1211061
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-27T20:51:41.063Z
- **Disclosed**: 2022-02-07T12:30:19.546Z

## Reporter
- **Username**: rohitburke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello team,
 
I have found one JSON path at  "https://lookup.nextcloud.com/"  which is leaking some information like Username, email id, version, etc.. 
I guess it show the user who have installed or configure anything through the vendor. I was also able to download some of the zip files of the vendor and much more.

--> Steps To Reproduce:
                  1) Go to this link "https://lookup.nextcloud.com/vendor/composer/installed.json" 
                  2) See the raw data, you will get leakage of some important data.

[
    {
        "name": "psr/http-message",
        "version": "1.0.1",
        "version_normalized": "1.0.1.0",
        "source": {
            "type": "git",
            "url": "https://github.com/php-fig/http-message.git",
            "reference": "f6561bf28d520154e4b0ec72be95418abe6d9363"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/php-fig/http-message/zipball/f6561bf28d520154e4b0ec72be95418abe6d9363",
            "reference": "f6561bf28d520154e4b0ec72be95418abe6d9363",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.0"
        },
        "time": "2016-08-06T14:39:51+00:00",
        "type": "library",
        "extra": {
            "branch-alias": {
                "dev-master": "1.0.x-dev"
            }
        },
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "Psr\\Http\\Message\\": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "PHP-FIG",
                "homepage": "http://www.php-fig.org/"
            }
        ],
        "description": "Common interface for HTTP messages",
        "homepage": "https://github.com/php-fig/http-message",
        "keywords": [
            "http",
            "http-message",
            "psr",
            "psr-7",
            "request",
            "response"
        ]
    },
    {
        "name": "pimple/pimple",
        "version": "v3.0.2",
        "version_normalized": "3.0.2.0",
        "source": {
            "type": "git",
            "url": "https://github.com/silexphp/Pimple.git",
            "reference": "a30f7d6e57565a2e1a316e1baf2a483f788b258a"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/silexphp/Pimple/zipball/a30f7d6e57565a2e1a316e1baf2a483f788b258a",
            "reference": "a30f7d6e57565a2e1a316e1baf2a483f788b258a",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.0"
        },
        "time": "2015-09-11T15:10:35+00:00",
        "type": "library",
        "extra": {
            "branch-alias": {
                "dev-master": "3.0.x-dev"
            }
        },
        "installation-source": "dist",
        "autoload": {
            "psr-0": {
                "Pimple": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "Fabien Potencier",
                "email": "fabien@symfony.com"
            }
        ],
        "description": "Pimple, a simple Dependency Injection Container",
        "homepage": "http://pimple.sensiolabs.org",
        "keywords": [
            "container",
            "dependency injection"
        ]
    },
    {
        "name": "psr/container",
        "version": "1.0.0",
        "version_normalized": "1.0.0.0",
        "source": {
            "type": "git",
            "url": "https://github.com/php-fig/container.git",
            "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/php-fig/container/zipball/b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
            "reference": "b7ce3b176482dbbc1245ebf52b181af44c2cf55f",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.0"
        },
        "time": "2017-02-14T16:28:37+00:00",
        "type": "library",
        "extra": {
            "branch-alias": {
                "dev-master": "1.0.x-dev"
            }
        },
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "Psr\\Container\\": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "PHP-FIG",
                "homepage": "http://www.php-fig.org/"
            }
        ],
        "description": "Common Container Interface (PHP FIG PSR-11)",
        "homepage": "https://github.com/php-fig/container",
        "keywords": [
            "PSR-11",
            "container",
            "container-interface",
            "container-interop",
            "psr"
        ]
    },
    {
        "name": "container-interop/container-interop",
        "version": "1.2.0",
        "version_normalized": "1.2.0.0",
        "source": {
            "type": "git",
            "url": "https://github.com/container-interop/container-interop.git",
            "reference": "79cbf1341c22ec75643d841642dd5d6acd83bdb8"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/container-interop/container-interop/zipball/79cbf1341c22ec75643d841642dd5d6acd83bdb8",
            "reference": "79cbf1341c22ec75643d841642dd5d6acd83bdb8",
            "shasum": ""
        },
        "require": {
            "psr/container": "^1.0"
        },
        "time": "2017-02-14T19:40:03+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "Interop\\Container\\": "src/Interop/Container/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "description": "Promoting the interoperability of container objects (DIC, SL, etc.)",
        "homepage": "https://github.com/container-interop/container-interop"
    },
    {
        "name": "nikic/fast-route",
        "version": "v1.2.0",
        "version_normalized": "1.2.0.0",
        "source": {
            "type": "git",
            "url": "https://github.com/nikic/FastRoute.git",
            "reference": "b5f95749071c82a8e0f58586987627054400cdf6"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/nikic/FastRoute/zipball/b5f95749071c82a8e0f58586987627054400cdf6",
            "reference": "b5f95749071c82a8e0f58586987627054400cdf6",
            "shasum": ""
        },
        "require": {
            "php": ">=5.4.0"
        },
        "time": "2017-01-19T11:35:12+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "FastRoute\\": "src/"
            },
            "files": [
                "src/functions.php"
            ]
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "BSD-3-Clause"
        ],
        "authors": [
            {
                "name": "Nikita Popov",
                "email": "nikic@php.net"
            }
        ],
        "description": "Fast request router for PHP",
        "keywords": [
            "router",
            "routing"
        ]
    },
    {
        "name": "slim/slim",
        "version": "3.8.1",
        "version_normalized": "3.8.1.0",
        "source": {
            "type": "git",
            "url": "https://github.com/slimphp/Slim.git",
            "reference": "5385302707530b2bccee1769613ad769859b826d"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/slimphp/Slim/zipball/5385302707530b2bccee1769613ad769859b826d",
            "reference": "5385302707530b2bccee1769613ad769859b826d",
            "shasum": ""
        },
        "require": {
            "container-interop/container-interop": "^1.2",
            "nikic/fast-route": "^1.0",
            "php": ">=5.5.0",
            "pimple/pimple": "^3.0",
            "psr/container": "^1.0",
            "psr/http-message": "^1.0"
        },
        "provide": {
            "psr/http-message-implementation": "1.0"
        },
        "require-dev": {
            "phpunit/phpunit": "^4.0",
            "squizlabs/php_codesniffer": "^2.5"
        },
        "time": "2017-03-19T17:55:20+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "Slim\\": "Slim"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "Rob Allen",
                "email": "rob@akrabat.com",
                "homepage": "http://akrabat.com"
            },
            {
                "name": "Josh Lockhart",
                "email": "hello@joshlockhart.com",
                "homepage": "https://joshlockhart.com"
            },
            {
                "name": "Gabriel Manricks",
                "email": "gmanricks@me.com",
                "homepage": "http://gabrielmanricks.com"
            },
            {
                "name": "Andrew Smith",
                "email": "a.smith@silentworks.co.uk",
                "homepage": "http://silentworks.co.uk"
            }
        ],
        "description": "Slim is a PHP micro framework that helps you quickly write simple yet powerful web applications and APIs",
        "homepage": "https://slimframework.com",
        "keywords": [
            "api",
            "framework",
            "micro",
            "router"
        ]
    },
    {
        "name": "guzzlehttp/promises",
        "version": "v1.3.1",
        "version_normalized": "1.3.1.0",
        "source": {
            "type": "git",
            "url": "https://github.com/guzzle/promises.git",
            "reference": "a59da6cf61d80060647ff4d3eb2c03a2bc694646"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/guzzle/promises/zipball/a59da6cf61d80060647ff4d3eb2c03a2bc694646",
            "reference": "a59da6cf61d80060647ff4d3eb2c03a2bc694646",
            "shasum": ""
        },
        "require": {
            "php": ">=5.5.0"
        },
        "require-dev": {
            "phpunit/phpunit": "^4.0"
        },
        "time": "2016-12-20T10:07:11+00:00",
        "type": "library",
        "extra": {
            "branch-alias": {
                "dev-master": "1.4-dev"
            }
        },
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "GuzzleHttp\\Promise\\": "src/"
            },
            "files": [
                "src/functions_include.php"
            ]
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "Michael Dowling",
                "email": "mtdowling@gmail.com",
                "homepage": "https://github.com/mtdowling"
            }
        ],
        "description": "Guzzle promises library",
        "keywords": [
            "promise"
        ]
    },
    {
        "name": "guzzlehttp/psr7",
        "version": "1.4.2",
        "version_normalized": "1.4.2.0",
        "source": {
            "type": "git",
            "url": "https://github.com/guzzle/psr7.git",
            "reference": "f5b8a8512e2b58b0071a7280e39f14f72e05d87c"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/guzzle/psr7/zipball/f5b8a8512e2b58b0071a7280e39f14f72e05d87c",
            "reference": "f5b8a8512e2b58b0071a7280e39f14f72e05d87c",
            "shasum": ""
        },
        "require": {
            "php": ">=5.4.0",
            "psr/http-message": "~1.0"
        },
        "provide": {
            "psr/http-message-implementation": "1.0"
        },
        "require-dev": {
            "phpunit/phpunit": "~4.0"
        },
        "time": "2017-03-20T17:10:46+00:00",
        "type": "library",
        "extra": {
            "branch-alias": {
                "dev-master": "1.4-dev"
            }
        },
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "GuzzleHttp\\Psr7\\": "src/"
            },
            "files": [
                "src/functions_include.php"
            ]
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "Michael Dowling",
                "email": "mtdowling@gmail.com",
                "homepage": "https://github.com/mtdowling"
            },
            {
                "name": "Tobias Schultze",
                "homepage": "https://github.com/Tobion"
            }
        ],
        "description": "PSR-7 message implementation that also provides common utility methods",
        "keywords": [
            "http",
            "message",
            "request",
            "response",
            "stream",
            "uri",
            "url"
        ]
    },
    {
        "name": "guzzlehttp/guzzle",
        "version": "6.2.3",
        "version_normalized": "6.2.3.0",
        "source": {
            "type": "git",
            "url": "https://github.com/guzzle/guzzle.git",
            "reference": "8d6c6cc55186db87b7dc5009827429ba4e9dc006"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/guzzle/guzzle/zipball/8d6c6cc55186db87b7dc5009827429ba4e9dc006",
            "reference": "8d6c6cc55186db87b7dc5009827429ba4e9dc006",
            "shasum": ""
        },
        "require": {
            "guzzlehttp/promises": "^1.0",
            "guzzlehttp/psr7": "^1.4",
            "php": ">=5.5"
        },
        "require-dev": {
            "ext-curl": "*",
            "phpunit/phpunit": "^4.0",
            "psr/log": "^1.0"
        },
        "time": "2017-02-28T22:50:30+00:00",
        "type": "library",
        "extra": {
            "branch-alias": {
                "dev-master": "6.2-dev"
            }
        },
        "installation-source": "dist",
        "autoload": {
            "files": [
                "src/functions_include.php"
            ],
            "psr-4": {
                "GuzzleHttp\\": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "Michael Dowling",
                "email": "mtdowling@gmail.com",
                "homepage": "https://github.com/mtdowling"
            }
        ],
        "description": "Guzzle is a PHP HTTP client library",
        "homepage": "http://guzzlephp.org/",
        "keywords": [
            "client",
            "curl",
            "framework",
            "http",
            "http client",
            "rest",
            "web service"
        ]
    },
    {
        "name": "abraham/twitteroauth",
        "version": "0.7.2",
        "version_normalized": "0.7.2.0",
        "source": {
            "type": "git",
            "url": "https://github.com/abraham/twitteroauth.git",
            "reference": "119d5a83478a2d21c09cd27980ab67eba11c8fe1"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/abraham/twitteroauth/zipball/119d5a83478a2d21c09cd27980ab67eba11c8fe1",
            "reference": "119d5a83478a2d21c09cd27980ab67eba11c8fe1",
            "shasum": ""
        },
        "require": {
            "ext-curl": "*",
            "php": "^5.6 || ^7.0"
        },
        "require-dev": {
            "phpmd/phpmd": "~2.4",
            "phpunit/phpunit": "~5.6",
            "squizlabs/php_codesniffer": "~2.7"
        },
        "time": "2016-12-12T17:42:13+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "Abraham\\TwitterOAuth\\": "src"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "Abraham Williams",
                "email": "abraham@abrah.am",
                "homepage": "https://abrah.am",
                "role": "Developer"
            }
        ],
        "description": "The most popular PHP library for use with the Twitter OAuth REST API.",
        "homepage": "https://twitteroauth.com",
        "keywords": [
            "Twitter API",
            "Twitter oAuth",
            "api",
            "oauth",
            "rest",
            "social",
            "twitter"
        ]
    }
]



--> Mitigation:
             Don't allow a user to access this path you can give some forbideen error to  the infected url.

--> Supporting Material/References:  
                     #159526 #10841

## Impact

-> Giving the information of users and vendors their product version, email address etc.

## Attachments
No attachments
