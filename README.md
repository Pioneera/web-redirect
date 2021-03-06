<h1  align="center">Welcome to web-redirect 👋</h1>
<p>
<img  alt="Version"  src="https://img.shields.io/badge/version-1.0.3-blue.svg?cacheSeconds=2592000"  />
<a  href="http://www.apache.org/licenses/LICENSE-2.0"  target="_blank">
<img  alt="License: APACHE--2"  src="https://img.shields.io/badge/License-APACHE--2-yellow.svg"  />
</a>
<a  href="https://twitter.com/troykelly"  target="_blank">
<img  alt="Twitter: troykelly"  src="https://img.shields.io/twitter/follow/troykelly.svg?style=social"  />
</a>
</p>

> Universal redirector designed for deployment in Google Cloud Run

### 🏠 [Homepage](https://github.com/Pioneera/web-redirect)

## Assumptions

You have a Google Cloud account, you have enabled billing and Google Cloud Run.

## Usage

If you just want to deploy and get running - copy `.env.example` to `.env` and update the information.

Once that is up-to-date - just run `./deploy.sh` and your project will be deployed

## Configuration

### .env example

```text
SERVICE_NAME=service-name
REGION=australia-southeast1
PROJECT_ID=project-id
REDIRECT_TYPE=302
REDIRECT_TARGET=https://pioneera.com/
GA=UAXXXXXXX
```

| Variable          | Required | Note                                                                                                   |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `SERVICE_NAME`    | No       | Cloud Run service name (only needed if using `./deploy.sh`)                                            |
| `REGION`          | No       | Cloud Run region (only needed if using `./deploy.sh`)                                                  |
| `PROJECT_ID`      | No       | Cloud Run project ID (only needed if using `./deploy.sh`)                                              |
| `REDIRECT_TYPE`   | Yes      | the [HTTP redirect code](https://en.wikipedia.org/wiki/URL_redirection#HTTP_status_codes_3xx) eg `302` |
| `REDIRECT_TARGET` | Yes      | the URL to redirect to                                                                                 |
| `GA`              | No       | Google Analytics tracking ID eg `UA-000000-2`                                                          |

## Author

👤 **Troy Kelly**

- Website: http://troykelly.com/
- Keybase: [@troykelly](https://keybase.io/troykelly)
- Twitter: [@troykelly](https://twitter.com/troykelly)
- Github: [@troykelly](https://github.com/troykelly)
- LinkedIn: [@troykelly](https://linkedin.com/in/troykelly)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br  />Feel free to check [issues page](https://github.com/Pioneera/web-redirect/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Pioneera Pty Ltd](https://github.com/Pioneera).<br  />
This project is [APACHE--2](http://www.apache.org/licenses/LICENSE-2.0) licensed.

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
