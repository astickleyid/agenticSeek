# Deployment Guide

## GitHub Pages Deployment

This repository is configured to automatically deploy the frontend to GitHub Pages.

### How it works

1. The GitHub Actions workflow (`.github/workflows/deploy-pages.yml`) automatically triggers on:
   - Push to the `main` branch
   - Manual workflow dispatch

2. The workflow:
   - Checks out the repository
   - Sets up Node.js
   - Installs dependencies for the React frontend
   - Builds the production bundle
   - Deploys to GitHub Pages

### Accessing the deployed site

Once deployed, the site will be available at:
- **Production URL**: https://astickleyid.github.io/agenticSeek

### Configuration

The `package.json` in `frontend/agentic-seek-front` contains the `homepage` field set to the GitHub Pages URL. This ensures all asset paths are correctly generated during the build.

### Important Notes

- The GitHub Pages deployment hosts only the **static frontend** of AgenticSeek
- The frontend requires a backend API to function properly (default: `http://localhost:7777`)
- For full functionality, users need to:
  1. Run the backend locally or on a server
  2. Configure the backend URL in their environment
  
### Manual Deployment

To manually trigger a deployment:
1. Go to the repository's Actions tab
2. Select the "Build and Deploy to GitHub Pages" workflow
3. Click "Run workflow"
4. Choose the branch (typically `main`)
5. Click "Run workflow"

### Local Testing

To test the production build locally:

```bash
cd frontend/agentic-seek-front
npm install
npm run build
npx serve -s build
```

This will serve the production build at `http://localhost:3000` (or another port if 3000 is in use).

### Troubleshooting

If the deployment fails:
1. Check the Actions tab for error logs
2. Ensure GitHub Pages is enabled in repository settings
3. Verify that the workflow has necessary permissions (`pages: write`, `id-token: write`)
4. Check that the `package.json` homepage field matches your repository

### Updating the Deployment

To update the deployed site, simply push changes to the `main` branch. The workflow will automatically rebuild and redeploy.
