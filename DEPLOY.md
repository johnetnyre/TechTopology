# Deploying Tech Topology to GitHub Pages

## 1. Create the repository

Create a GitHub repository such as `TechTopology`. A public repository works with GitHub Pages on GitHub Free; other GitHub plans can also publish Pages from private repositories depending on plan and organization settings.

## 2. Upload this project

Upload everything in this folder except `_site/` (it is generated automatically and is ignored by Git).

If using the command line:

```bash
git init
git add .
git commit -m "Initial Tech Topology site"
git branch -M main
git remote add origin https://github.com/YOUR-ACCOUNT/TechTopology.git
git push -u origin main
```

## 3. Enable Pages

In the GitHub repository:

1. Open **Settings**.
2. Select **Pages**.
3. Under **Build and deployment**, choose **GitHub Actions** as the source.
4. Open the **Actions** tab and watch `Build, test, and deploy GitHub Pages`.

The included workflow builds the site, validates the HTML, runs Pa11y WCAG 2 AA checks, uploads the generated `_site` directory, and deploys it.

## 4. Find the site

For a repository named `TechTopology`, GitHub will normally publish a project site at a URL shaped like:

`https://YOUR-ACCOUNT.github.io/TechTopology/`

The build uses GitHub's supplied Pages base path automatically, so no URL edits are required.

## 5. Optional custom domain

After Georgia Tech approves the DNS configuration, add the custom domain in **Settings → Pages → Custom domain**. Configure DNS according to GitHub Pages documentation. Do not rely on a manually committed `CNAME` file as the only configuration step.

A possible institutional URL would be something like `techtopology.gatech.edu`, subject to Georgia Tech DNS and web-governance approval.

## 6. Editing the conference

For ordinary updates, edit the YAML files under `_data/`, commit, and push. GitHub Actions rebuilds the site automatically. See `README.md` for the annual-update checklist.
