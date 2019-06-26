# Standard Charges Data

Sources of hospital data in compliance with CMS manadate.

## Contributions

If you would like to contribute to this master list, there are a few "rules" that we ask you to follow to keep this list organized.

1. At this time, we are supporting csv, json and xls files. We have found a number of hospitals are exporting these data in Word documents.  If you have recommendations on how to approach this, see the "Join us online" section below.

2. All records MUST have the following fields populated:

  - State
  - County
  - City
  - Hospital
  - Url

3. Where possible, always use "https" as the protocol in the url.  Sometimes the default link will be "http," yet "https" works.  If it works, please use it.

4. For now, the url files will be csv.  

5. Scripts must be in R or Python 3.  It would be nice to have both, but one will suffice.  We have sample script repositories for Python and R, and we will try our best to maintain both at the same level of functionality.  It is recommended to format Python code so that it supports [interactive Python](https://code.visualstudio.com/docs/python/jupyter-support) in Visual Studio Code.  We also prefer [RMarkdown](https://rmarkdown.rstudio.com/) in sample scripts.

6. Contributions will be handled through [Pull Request](https://help.github.com/en/articles/about-pull-requests).  If you don't even know what git is, we recommend finding someone to help you get started and mentor you as you begin to code.  If you need help finding someone, see the "Join us online" section below.

## Roadmaps and Plans

1. We do not know what we are getting into.  We are just getting started. A couple of friends having breakfast started discussing ideas to help health services researchers, and now we are doing it.  The hope is that we might help save a hospital one day, particularly in a rural area.

2. These data files do not appear friendly, or anywhere close to following a standard.  Maybe this is something we do as a project: encourage hospitals to follow a standard format and approach.  If you are interested in helping to formulate a voluntary standard, see below.

3. We are not sure how much variability there will be in the fields between files.  Even though we produce a consolidated list of file locations, we will have a major normalization challenge.

4. We know that charge descriptions are also all over the place.  We expect a significant effort in normalizing descriptions.  Hopefully we can utilize standardized terminologies, vocabularies and nomenclatures to facilitate comparisons across the health care system.

5. As data sources are consolidated, we hope to begin analysis and visualization of these data.  We are learning.  We are advancing our skills and techniques in data science.  You can learn too.  Please participate and share.

## Join Us Online

You can join the `#ohana-contributor` channel on the informaticist slack workspace (informaticist.slack.com).  Contact contrib@ohanaproject.org for an invitation.

You can email contrib@ohanaproject.org

You can tweet us @OhanaProjectOrg

## For Code Issues

You can open an issue at the Ohana Project on Github.

## Conduct and Inclusion

We aren't big enough to have committees and formal policies yet, but no contribution is worth it if others are hurt in the process.

To borrow from the [PyCon Code of Conduct](https://github.com/python/pycon-code-of-conduct/blob/master/code_of_conduct.md):
  > We welcome everyone, regardless of age, gender identity and expression, sexual orientation, disability, physical appearance, body size, ethnicity, nationality, race, or religion (or lack thereof), education, or socio-economic status.

We welcome you to show up, to try, to ask questions, and make many mistakes.  Just limit the mistakes to the code.  Inappropriate behavior directed at others, regardless of where it happens, means that you can't participate here.  We are focused on health care and helping people.

If you have an issue with someone's behavior, please contact director@ohanaproject.org
