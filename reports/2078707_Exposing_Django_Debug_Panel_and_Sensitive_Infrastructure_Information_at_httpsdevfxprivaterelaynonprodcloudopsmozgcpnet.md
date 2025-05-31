# Exposing Django Debug Panel and Sensitive Infrastructure Information at https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net

## Report Details
- **Report ID**: 2078707
- **URL**: https://hackerone.com/reports/2078707
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-07-21T09:40:51.000Z
- **Disclosed**: 2023-10-13T14:02:13.325Z

## Reporter
- **Username**: aliend89
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
This security report highlights the critical risks and issues associated with exposing the Django Debug Panel in a development environment available at https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net. The Django Debug Panel is a powerful tool used during application development, but enabling it in a development environment without proper access controls can lead to significant security vulnerabilities. The primary concern is the exposure of sensitive information about the infrastructure, such as the locations of Redis and PostgreSQL databases, user information, internal IP addresses and other details that can be exploited by attackers to launch potential attack vectors.

## Steps To Reproduce:
Access the following URLs:
- https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net//app/tmp/healthcheck.json
- https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net/fxa-rp-events

where you can find the full configuration exposed. The most interesting are:
```
ADMIN_ENABLED 	
True
ALLOWED_HOSTS 	
['dev.fxprivaterelay.nonprod.cloudops.mozgcp.net',
 'privacydev.fxprivaterelay.nonprod.cloudops.mozgcp.net']

AUTHENTICATION_BACKENDS 	
('django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend')
AUTH_USER_MODEL 	
'auth.User'
AVATAR_IMG_SRC 	
['mozillausercontent.com', 'https://profile.stage.mozaws.net']
AVATAR_IMG_SRC_MAP 	
{'https://profile.accounts.firefox.com/v1': ['firefoxusercontent.com',
                                             'https://profile.accounts.firefox.com'],
 'https://profile.stage.mozaws.net/v1': ['mozillausercontent.com',
                                         'https://profile.stage.mozaws.net']}
AWS_REGION 	
'us-east-1'
AWS_SES_CONFIGSET 	
'dev_fxprivaterelay_nonprod_cloudops_mozgcp_net'
AWS_SNS_TOPIC 	
{'arn:aws:sns:us-east-1:927034868273:fxprivaterelay-SES-processor-topic'}
AWS_SQS_EMAIL_QUEUE_URL 	
'██████████'
AWS_SQS_QUEUE_URL 	
'█████████'
BASKET_ORIGIN 	
'https://basket-dev.allizom.org'
BUNDLE_PLAN_ID_US 	
'price_1LwoSDJNcmPzuWtR6wPJZeoh'
CACHES 	
{'default': {'BACKEND': 'django_redis.cache.RedisCache',
             'LOCATION': '████:19509',
             'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient'}}}
CORS_ALLOWED_ORIGINS 	
['https://vault.bitwarden.com', 'https://vault.qa.bitwarden.pw']
DATABASES 	
{'default': {'ATOMIC_REQUESTS': False,
             'AUTOCOMMIT': True,
             'CONN_HEALTH_CHECKS': False,
             'CONN_MAX_AGE': 0,
             'ENGINE': 'django.db.backends.postgresql',
             'HOST': 'ec2-23-20-140-229.compute-1.amazonaws.com',
             'NAME': 'dav509dnmoe86f',
             'OPTIONS': {},
             'PASSWORD': '********************',
             'PORT': 5432,
             'TEST': {'CHARSET': None,
                      'COLLATION': None,
                      'MIGRATE': True,
                      'MIRROR': None,
                      'NAME': None},
             'TIME_ZONE': None,
             'USER': 'zqhdtlumxotgdr'}}
INSTALLED_APPS 	
['whitenoise.runserver_nostatic',
 'django.contrib.staticfiles',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.sites',
 'django_filters',
 'django_ftl.apps.DjangoFtlConfig',
 'dockerflow.django',
 'allauth',
 'allauth.account',
 'allauth.socialaccount',
 'allauth.socialaccount.providers.fxa',
 'rest_framework',
 'rest_framework.authtoken',
 'corsheaders',
 'waffle',
 'privaterelay.apps.PrivateRelayConfig',
 'api.apps.ApiConfig',
 'drf_spectacular',
 'drf_spectacular_sidecar',
 'debug_toolbar',
 'django.contrib.admin',
 'emails.apps.EmailsConfig',
 'phones.apps.PhonesConfig']
INTERNAL_IPS 	
['███████']
LOGGING 	
{'formatters': {'json': {'()': 'dockerflow.logging.JsonLogFormatter',
                         'logger_name': 'fx-private-relay'}},
 'handlers': {'console_err': {'class': 'logging.StreamHandler',
                              'formatter': 'json',
                              'level': 'DEBUG'},
              'console_out': {'class': 'logging.StreamHandler',
                              'formatter': 'json',
                              'level': 'DEBUG',
                              'stream': <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>}},
 'loggers': {'abusemetrics': {'handlers': ['console_out'], 'level': 'INFO'},
             'events': {'handlers': ['console_err'], 'level': 'ERROR'},
             'eventsinfo': {'handlers': ['console_out'], 'level': 'INFO'},
             'markus': {'handlers': ['console_out'], 'level': 'DEBUG'},
             'request.summary': {'handlers': ['console_out'], 'level': 'DEBUG'},
             'studymetrics': {'handlers': ['console_out'], 'level': 'INFO'}},
 'version': 1}
REST_FRAMEWORK 	
{'DEFAULT_AUTHENTICATION_CLASSES': ['api.authentication.FxaTokenAuthentication',
                                    'rest_framework.authentication.TokenAuthentication',
                                    'rest_framework.authentication.SessionAuthentication'],
 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
 'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer',
                              'rest_framework.renderers.BrowsableAPIRenderer'],
 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
 'EXCEPTION_HANDLER': 'api.views.relay_exception_handler'}
```

## Impact

Enabling the Django Debug Panel in a development environment without proper access controls can result in the following vulnerabilities and risks:
- Sensitive Information Exposure: The Debug Panel may reveal sensitive details about the application's infrastructure, including the locations of Redis and PostgreSQL databases, user information, secret keys, and other critical data. Attackers can exploit this information to identify potential vulnerabilities and plan targeted attacks against the production environment.
- Database Information Disclosure: Database queries and their execution times are exposed through the Debug Panel. This information can be used by attackers to gather insights into the database schema and structure, enabling them to plan SQL injection or data extraction attacks.
- System Enumeration and Reconnaissance: Details such as server environment variables and file paths can assist attackers in performing system enumeration and reconnaissance. This knowledge can be utilized to discover weaknesses and potential entry points into the system.
- Potentially Unpatched Vulnerabilities: Enabling the Debug Panel in a development environment may also expose unpatched vulnerabilities or misconfigurations that could have been addressed before moving the application to production. Attackers can exploit these vulnerabilities to gain unauthorized access.

## Attachments
No attachments
