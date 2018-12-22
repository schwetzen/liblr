# liblr

[![Build Status](https://travis-ci.org/schwetzen/liblr.svg?branch=dev)](https://travis-ci.org/schwetzen/liblr)

Liblr is a web application that can be used as a replacement for your browser
bookmarks and paper notes for storing information about interesting articles,
websites, books or you name it. You can store all of your reading tips in a
centralized place.

Head over to https://schwetzen.com to begin.

For the project report, see [REPORT.md](https://github.com/schwetzen/liblr/blob/master/REPORT.md).

## Account, Email & GDPR

The software currently requires you register and log in using an email address.
We do not send you any emails, it is just used as a username.

Be aware that since the project is a course project we are not GDPR compliant.
At the moment there is no way for you to delete or inspect your account or data.
If you wish to do so, please contact daniel.riissanen[at]gmail.com.

## How do I run it?

**Requirements**

- Python 3.5+ (3.7 recommended)
- `venv` as the virtual environment

The production site is https://schwetzen.com, but if you wish to test the
software yourself, feel free to clone this repository
```
~$ git clone https://github.com/schwetzen/liblr.git
```
and run the commands
```
~/liblr$ make update
~/liblr$ make run  # make test, to run the tests
```
to start a local server instance.

## Course specific information

This is a project made for a software development course at The University of
Helsinki and this section contains the necessary documents and links for that.

### Definition of Done
- The acceptance criteria have been met
- New code has been reviewed by at least one other team member
- Build at Travis has completed successfully

### Useful links
- [Product backlog](https://docs.google.com/spreadsheets/d/15EXXftlXvssDdknBq9nNkMCjH7mDnwAeK0zw14V76M8/edit?usp=sharing)
- [Sprint 1 backlog](https://docs.google.com/spreadsheets/d/14ZnelNYfI1DPEMyDz9Tm0RVpIi0oDKOS8HHnhe32Zh0/edit?usp=sharing)
- [Sprint 2 backlog](https://docs.google.com/spreadsheets/d/11PPuZSJEFHD_mbAesJxFxLXXr89taoT3hm0w2X60JVA/edit?usp=sharing)
- [Sprint 3 backlog](https://docs.google.com/spreadsheets/d/1nEZxifxYrckJiFKRFn_WfPdEwU8H2xoJn6IvMP-y_3o/edit?usp=sharing)
- [Sprint 4 backlog](https://docs.google.com/spreadsheets/d/1BbaP8Sp3omkdu1VbbiKDqqaruQUbwbUS7gOdtrMv4Ps/edit?usp=sharing)
- [Burndown chart](https://docs.google.com/spreadsheets/d/1Gn-kzJeadceD5dZH-4P0hI_JCB0PMYjwW80lVVSa_AQ/edit?usp=sharing)
- [Project report](https://github.com/schwetzen/liblr/blob/master/REPORT.md)
