# drf-test

# Ultimate Goal

- [ ] Authentication
    - [ ] JWT
    - [ ] OAuth2 (Google)
- [ ] Security
    - [ ] HMAC
    - [ ] CSRF
    - [ ] CSP
- [ ] Function
    - [ ] Login
    - [ ] Task Queue
    - [ ] Translate
        - [ ] Query
        - [ ] History by date
        - [ ] History by user
- [ ] Performance
    - [ ] Redis
- [ ] Deploy
    - [ ] uwsgi
    - [ ] gunicorn
    - [ ] nginx
- [ ] Cloud
    - [ ] AWS
    - [ ] GCP

# API Flow

```mermaid
graph LR;
    API-->Routers;
    Routers-->Permissions;
    subgraph View
        Permissions-->Validators;
        Validators-->Serializers;
    end
    Serializers<-->ORM;
    ORM<-->DB;
```

# GCP translate API

1. Login GCP
2. Enable "Cloud Translation API"
3. Install gcloud sdk
4. login gcloud
    ```bash
    $ gcloud auth login
    ```

# Reference

- [Build django-rest-framework](https://medium.com/bandai%E7%9A%84%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98/%E6%89%8B%E6%8A%8A%E6%89%8B%E7%A8%8B%E5%BC%8F%E5%AF%A6%E4%BD%9C%E5%88%86%E4%BA%AB%E7%B3%BB%E5%88%97-%E5%BB%BA%E6%A7%8B-django-rest-framework-drf-api-bf7e6e1997e4)
- [django-rest-framework tutorial](https://www.django-rest-framework.org/tutorial/quickstart/)
- [django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/getting_started.html)
- [Troubleshoot your ADC setup](https://cloud.google.com/docs/authentication/troubleshoot-adc#user-creds-client-based)
