# Generate SEO optimized header tags for Hugo generated websites

A GitHub Action that generates the proper SEO tags for published websites generated by a separate Action.

## Use

```yaml
on:
  push:
    branches:
    - master
jobs:
  generateSeoTags:
    name: Generate published websites seo tags
    runs-on: ubuntu-latest
    steps:

    - uses: actions/checkout@master
      with:
        submodules: true

    - name: Setup Hugo
      uses: peaceiris/actions-hugo@v2.2.2
      with:
        hugo-version: '0.58.3'
        # extended: true

    - name: Build
      run: hugo --gc --minify --cleanDestinationDir -e production

    - name: Update seo tags
      uses: bw-gaming/nxt-hugo-actions-seo@master

    - name: Publish to Pages
      uses: peaceiris/actions-gh-pages@v1.0.1
      env:
        ACTIONS_DEPLOY_KEY: ${{ secrets.ACTIONS_DEPLOY_KEY }}
        PUBLISH_DIR: ./doc
        PUBLISH_BRANCH: gh-pages
```

## Configuration

| Key | Description | Type | Required |
|-----|-------------|------|----------|
| `PUBLISH_DIR` | Directory where the hugo website is generated. _(Defaults to `$GITHUB_WORKSPACE/public`)_ | `env` | No |

## License

[MIT](LICENSE.md)
