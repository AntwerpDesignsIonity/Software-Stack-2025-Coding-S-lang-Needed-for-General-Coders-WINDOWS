# Branch Renaming Instructions: Root-Main → SEED

## Overview
This document provides step-by-step instructions for renaming the default branch from **Root-Main** to **SEED** and establishing a clean branch structure.

## Current State
- **Current Default Branch:** `Root-Main`
- **Target Default Branch:** `SEED`

## Why Rename to SEED?
The SEED branch represents the foundational, stable codebase from which all development branches will grow. This naming convention better reflects the purpose of the main branch as the starting point for all development work.

## Step-by-Step Renaming Process

### Prerequisites
- Repository administrator access
- All team members notified of the upcoming change
- All open pull requests should be noted (they will need to be retargeted)

### Instructions for Repository Administrators

#### Option 1: Using GitHub Web Interface (Recommended)

1. **Navigate to Repository Settings**
   - Go to your repository on GitHub
   - Click on **Settings** tab
   - Click on **Branches** in the left sidebar

2. **Rename the Default Branch**
   - Find the "Default branch" section
   - Click the pencil icon (✏️) or "Rename branch" button next to `Root-Main`
   - Enter the new branch name: `SEED`
   - Click "Rename branch"
   - Confirm the action in the dialog box

3. **GitHub Will Automatically:**
   - Update all open pull requests to target the new branch name
   - Update branch protection rules
   - Redirect references from the old branch name to the new one

#### Option 2: Using Git Command Line

If you prefer using the command line:

```bash
# Step 1: Rename the local branch
git branch -m Root-Main SEED

# Step 2: Delete the old remote branch
git push origin --delete Root-Main

# Step 3: Push the renamed branch
git push origin SEED

# Step 4: Reset the upstream branch for the new name
git push origin -u SEED
```

**Note:** After using the command line method, you still need to update the default branch setting in GitHub Settings → Branches.

### Post-Rename Actions

#### For Repository Administrators
1. Verify the default branch is now set to `SEED` in repository settings
2. Check that branch protection rules are applied to `SEED`
3. Review all open pull requests to ensure they target the correct branch
4. Update any CI/CD configurations that reference the old branch name
5. Update documentation and README files that mention the branch name

#### For Team Members
All team members with local clones of the repository should run:

```bash
# Fetch the latest changes
git fetch origin

# Switch to the new branch name
git branch -m Root-Main SEED

# Update the upstream tracking
git branch -u origin/SEED SEED

# Verify the change
git branch -vv
```

### Updating Existing Pull Requests
- GitHub automatically updates PR targets when renaming through the web interface
- If done manually, update the base branch for each open PR:
  1. Go to the pull request
  2. Click "Edit" next to the base branch
  3. Select `SEED` as the new base

### Updating CI/CD and Workflows

If you have GitHub Actions or other CI/CD configured, update workflow files:

```yaml
# Before:
on:
  push:
    branches: [ Root-Main ]

# After:
on:
  push:
    branches: [ SEED ]
```

## Branching Strategy Post-Rename

### Proposed Branch Structure

```
SEED (default/main branch)
├── feature/feature-name
├── bugfix/bug-description  
├── hotfix/critical-fix
└── release/version-number
```

### Branch Naming Conventions

- **SEED**: Stable, production-ready code
- **feature/**: New features in development
- **bugfix/**: Bug fixes
- **hotfix/**: Critical fixes for production
- **release/**: Release preparation branches

## Verification Checklist

After completing the rename, verify:

- [ ] Default branch in GitHub settings shows `SEED`
- [ ] All open pull requests target `SEED`
- [ ] Branch protection rules are active on `SEED`
- [ ] CI/CD workflows reference `SEED`
- [ ] Team members have updated their local repositories
- [ ] Documentation updated to reference `SEED`
- [ ] README updated with new branch name

## Rollback Plan

If issues arise, you can revert:

```bash
# Rename back to Root-Main
git branch -m SEED Root-Main
git push origin --delete SEED
git push origin -u Root-Main
```

Then update the default branch back in GitHub Settings.

## FAQ

### Q: Will this break existing clones?
A: No. GitHub creates a redirect from the old branch name. However, users should update their local repositories using the commands provided above.

### Q: What happens to the commit history?
A: All commit history is preserved. Renaming a branch only changes its name, not its content or history.

### Q: Do I need to update my .git/config file?
A: If you follow the update commands, the config is updated automatically. You can verify with `git config -l`.

### Q: Will this affect webhooks or integrations?
A: Yes, update any webhooks, integrations, or external services that reference the old branch name.

## Support

For questions or issues during the rename process, contact:
- Repository Administrator: AntwerpDesignsIonity
- Issues: https://github.com/AntwerpDesignsIonity/Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS/issues

## Implementation Date
To be determined by repository administrators.

---

**Note:** This rename improves clarity and aligns with modern branching conventions where the main branch represents the "seed" or foundation of all development work.
