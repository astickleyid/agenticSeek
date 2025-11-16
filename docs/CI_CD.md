# CI/CD Documentation

This document describes the Continuous Integration and Continuous Deployment (CI/CD) setup for the AgenticSeek project.

## GitHub Actions Workflows

The project uses GitHub Actions for automated testing, code quality checks, and deployment. The workflows are located in `.github/workflows/`.

### 1. Python CI (`python-ci.yml`)

**Triggers:** Push and Pull Request to `main` branch, Manual workflow dispatch

**Purpose:** Tests the Python backend across multiple Python versions.

**Steps:**
- Tests against Python 3.10, 3.11, and 3.12
- Installs dependencies from `requirements.txt`
- Runs pytest with coverage reporting
- Uploads coverage reports to Codecov (for Python 3.10)

**Note:** Some dependencies (like PyAudio) may fail to install in CI environments. The workflow continues even if some non-critical dependencies fail to install.

### 2. Frontend CI (`frontend-ci.yml`)

**Triggers:** Push and Pull Request to `main` branch, Manual workflow dispatch

**Purpose:** Builds and validates the React frontend application.

**Steps:**
- Sets up Node.js 18
- Installs npm dependencies
- Builds the production frontend
- Uploads build artifacts (retained for 7 days)

### 3. Code Quality (`code-quality.yml`)

**Triggers:** Push and Pull Request to `main` branch, Manual workflow dispatch

**Purpose:** Enforces code quality standards for both Python and JavaScript code.

**Python Linting:**
- Runs `flake8` for syntax and style checking
- Runs `black` for code formatting verification
- Runs `isort` for import sorting verification

**Frontend Linting:**
- Runs ESLint (through the build process)

**Note:** Linting failures are currently set to `continue-on-error: true` to avoid blocking PRs. This can be changed to enforce stricter quality standards.

### 4. Deploy to GitHub Pages (`deploy-pages.yml`)

**Triggers:** Push to `main` branch, Manual workflow dispatch

**Purpose:** Builds and deploys the React frontend to GitHub Pages.

**Steps:**
- Builds the React application
- Configures GitHub Pages
- Uploads the build artifacts
- Deploys to GitHub Pages environment

**Access:** The deployed site is available at: `https://astickleyid.github.io/agenticSeek`

## Running Workflows Manually

All workflows can be triggered manually from the GitHub Actions tab:
1. Go to the "Actions" tab in the repository
2. Select the workflow you want to run
3. Click "Run workflow"
4. Select the branch and click "Run workflow"

## Local Development

### Frontend Build
```bash
cd frontend/agentic-seek-front
npm ci
npm run build
```

### Python Tests
```bash
pip install -r requirements.txt
pip install pytest pytest-cov
python -m pytest tests/ -v
```

### Code Quality Checks

**Python:**
```bash
pip install flake8 black isort
flake8 .
black --check .
isort --check-only .
```

**Frontend:**
```bash
cd frontend/agentic-seek-front
npm run build
```

## GitHub Pages Configuration

The GitHub Pages deployment is configured to:
- Deploy from the `gh-pages` branch (automatically managed by the workflow)
- Use the built React app from `frontend/agentic-seek-front/build`
- Base URL is set to `/agenticSeek/` (configured in package.json homepage)

### Required Repository Settings

For GitHub Pages to work, ensure:
1. GitHub Pages is enabled in repository Settings → Pages
2. Source is set to "GitHub Actions"
3. The workflow has write permissions for `contents`, `pages`, and `id-token`

## Contributing

When contributing to the project:
1. All workflows will run automatically on pull requests
2. Ensure your code passes the CI checks
3. The deployment workflow only runs on the `main` branch

## Troubleshooting

### Python CI Failures
- Check if all required dependencies are in `requirements.txt`
- Some system-level dependencies (like audio libraries) may not be available in CI
- The workflow is configured to continue even if some dependencies fail

### Frontend CI Failures
- Ensure `package-lock.json` is committed and up to date
- Check Node.js version compatibility
- Build errors will show in the workflow logs

### Deployment Failures
- Verify GitHub Pages is enabled in repository settings
- Check that the workflow has necessary permissions
- Ensure the homepage in package.json matches the repository name
