# hltv_api (WIP)
Since [HLTV.org](https://www.hltv.org) doesn't provide a public API, and recently with the rise in popularity of Machine Learning and Data Engineering, statistical datasets are more important day by day, I've decided to develop a humble project, targeting those who are in need of things like these. Stop wasting your time hand-collecting data, or incorporate this package in your webservice, whatever.

## DISCLAIMER
This is a **work-in-progress** project, so take those words wisely and this repository with a grain of salt. Decided for it to be a long-term, serious project, contributions are welcome. And yes, I'm well aware of the existing [Node.js based HLTV API Agent](https://github.com/gigobyte/HLTV) by [gigobyte](https://github.com/gigobyte) - the main reasons why I decided to go with another one from-scratch myself is:
- there are no Python-based solutions available online (that I so far know of)
- why not?

## Installation

### Virtual environment (venv) - Python 3.3+
If you prefer to use the virtual environment (*probably because WSL's compatibility with anything is dogshit*), you can create a virtual environment:
```bash
python -m venv ./hltv_api
source ./bin/activate

# To deactivate:
deactivate
```
