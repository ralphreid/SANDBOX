## PyPI for Mininet / Mininet Module Repository
The purpose of this project is to enable users to share their modules and have other users to be able to easily install it.

### Packaging Format
Before any modules can be shared, a packaging format has to be defined for Mininet modules first. We have decided that the Mininet packaging format is just a plain old Python packaging format based on `setuptools` and `distutils`.

For a quick peek at how to convert existing modules to this packaging system, take a look at my commits:
- `pox`: https://github.com/heryandi/pox/commits/for_riplpox
- `ripl`: https://github.com/heryandi/ripl/commits/master
- `riplpox`: https://github.com/heryandi/riplpox/commits/master


### Components
- A website, [Mininet Repo](https://github.com/heryandi/djangopypi2), deployed [here](https://ec2-54-218-16-158.us-west-2.compute.amazonaws.com/), documentation available [here](https://github.com/heryandi/gsoc2013-onl-mininet/wiki/Mininet-Repo-Docs). Test cases:
  - https://github.com/heryandi/djangopypi2/blob/gsoc/djangopypi2/apps/pypi_frontend/tests.py
  - https://github.com/heryandi/djangopypi2/blob/gsoc/djangopypi2/apps/pypi_packages/tests.py
  - https://github.com/heryandi/djangopypi2/blob/gsoc/djangopypi2/apps/pypi_users/tests.py
- Command-line tool, [mnp](https://github.com/heryandi/mnp), documentation available [here](https://github.com/heryandi/gsoc2013-onl-mininet/wiki/mnp:-Mininet-Packaging-Tools-Docs). Test cases [here](https://github.com/heryandi/mnp/tree/master/mnp/test).

---

## Full System Experiment Archive
The purpose of this project is to create a website for researchers to share with others VM image that is ready to run their experiment. This project is incomplete.

Code available [here](https://github.com/heryandi/experiment_repo).
Documentation available [here](https://github.com/heryandi/gsoc2013-onl-mininet/wiki/Experiment-Repo-Docs).

---

#### Old wiki page for this GSoC project kept [here](https://github.com/mininet/mininet/wiki/%5BGSoC-2013%5D-Web-Interface-for-Sharing-Mininet-Systems-%5BOld%5D).