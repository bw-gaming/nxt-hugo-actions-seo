FROM python:3.7.5-alpine3.10

LABEL "com.github.actions.name"="Generates seo tags documentation"
LABEL "com.github.actions.description"="Generates seo tags project documentation to be published"
LABEL "com.github.actions.icon"="link"
LABEL "com.github.actions.color"="blue"

LABEL "repository"="https://github.com/bw-gaming/bw-actions-hugo-seo"
LABEL "homepage"="https://github.com/bw-gaming/bw-actions-hugo-seo"
LABEL "maintainer"="bw-gaming@github.com"


RUN pip install beautifulsoup4==4.8.1

COPY ./entrypoint.sh .

ENTRYPOINT ["/entrypoint.sh"]
