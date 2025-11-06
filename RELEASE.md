# Release Instructions

This document describes how to release new versions of `conformal-clip-data` to PyPI using GitHub Actions.

## Prerequisites

### Set up PyPI Trusted Publishing (Recommended)

1. Go to your PyPI account settings: https://pypi.org/manage/account/publishing/
2. Add a new "pending publisher" with the following details:
   - PyPI Project Name: `conformal-clip-data`
   - Owner: `fmegahed` (or your GitHub username/organization)
   - Repository name: `conformal-clip-data`
   - Workflow name: `publish-to-pypi.yml`
   - Environment name: (leave blank)

### Alternative: Using PyPI API Token

If you prefer using an API token instead of trusted publishing:

1. Generate a PyPI API token at https://pypi.org/manage/account/token/
2. Add the token as a repository secret:
   - Go to your repository → Settings → Secrets and variables → Actions
   - Create a new secret named `PYPI_API_TOKEN`
   - Paste your API token as the value
3. Update `.github/workflows/publish-to-pypi.yml` to use the token:
   ```yaml
   - name: Publish to PyPI
     uses: pypa/gh-action-pypi-publish@release/v1
     with:
       password: ${{ secrets.PYPI_API_TOKEN }}
       skip-existing: true
       verbose: true
   ```

## Release Process

### 1. Update Version Number

Edit `pyproject.toml` and update the version number:

```toml
[project]
version = "0.2.0"  # Update this
```

### 2. Commit Changes

```bash
git add pyproject.toml
git commit -m "Bump version to 0.2.0"
git push origin main
```

### 3. Create and Push a Tag

```bash
git tag v0.2.0
git push origin v0.2.0
```

### 4. Monitor the Release

1. Go to your repository's Actions tab on GitHub
2. Watch the "Publish to PyPI" workflow run
3. Once completed, verify the package at https://pypi.org/project/conformal-clip-data/

### 5. Create GitHub Release (Optional)

1. Go to your repository's Releases page
2. Click "Draft a new release"
3. Select the tag you just created (e.g., `v0.2.0`)
4. Add release notes describing the changes
5. Publish the release

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **Major version** (x.0.0): Breaking changes or major new datasets
- **Minor version** (0.x.0): New datasets or significant additions
- **Patch version** (0.0.x): Bug fixes, documentation updates, minor improvements

## Troubleshooting

### Workflow fails with "403 Forbidden" on PyPI upload

- Ensure trusted publishing is set up correctly on PyPI
- Or verify your `PYPI_API_TOKEN` secret is set correctly

### Tag already exists

```bash
# Delete local tag
git tag -d v0.2.0

# Delete remote tag
git push --delete origin v0.2.0

# Recreate and push
git tag v0.2.0
git push origin v0.2.0
```

### Test workflow before release

You can test the build process locally:

```bash
pip install build twine
python -m build
twine check dist/*
```
