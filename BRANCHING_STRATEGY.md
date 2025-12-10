# Branching Strategy

## Overview
This repository uses a simplified branching strategy with **SEED** as the main branch (formerly Root-Main).

## Branch Structure

### Main Branch: SEED
- **Purpose:** Production-ready, stable code
- **Protection:** Protected branch (requires reviews for merges)
- **Naming:** `SEED`
- **Description:** The SEED branch contains the stable foundation code. All feature branches are created from SEED and merge back into it.

### Development Branches

#### Feature Branches
- **Naming Convention:** `feature/description`
- **Purpose:** New features or enhancements
- **Created From:** SEED
- **Merges Into:** SEED
- **Example:** `feature/add-python-installer`, `feature/add-readme-file`
- **Note:** Automated tools may use prefixes like `copilot/` or `bot/` - these follow the same workflow

#### Bug Fix Branches
- **Naming Convention:** `bugfix/description`
- **Purpose:** Bug fixes
- **Created From:** SEED
- **Merges Into:** SEED
- **Example:** `bugfix/fix-install-path`

#### Hotfix Branches
- **Naming Convention:** `hotfix/description`
- **Purpose:** Critical fixes that need immediate deployment
- **Created From:** SEED
- **Merges Into:** SEED
- **Example:** `hotfix/critical-security-patch`

#### Release Branches (Optional)
- **Naming Convention:** `release/v1.0.0`
- **Purpose:** Prepare releases
- **Created From:** SEED
- **Merges Into:** SEED
- **Example:** `release/v1.0.0`

## Workflow

### Creating a New Feature

```bash
# Update your local SEED branch
git checkout SEED
git pull origin SEED

# Create a new feature branch
git checkout -b feature/my-new-feature

# Make your changes and commit
git add .
git commit -m "Add new feature"

# Push to remote
git push origin feature/my-new-feature

# Create a Pull Request to SEED on GitHub
```

### Updating Your Branch

```bash
# Get latest changes from SEED
git checkout SEED
git pull origin SEED

# Switch back to your feature branch
git checkout feature/my-new-feature

# Merge or rebase SEED into your branch
git merge SEED
# or
git rebase SEED

# Push updates
git push origin feature/my-new-feature
```

### Merging to SEED

1. Create a Pull Request (PR) from your branch to SEED
2. Request review from team members
3. Address any feedback
4. Once approved, merge the PR
5. Delete the feature branch (optional but recommended)

## Branch Protection Rules for SEED

Recommended protection rules for the SEED branch:

- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- ✅ Include administrators in these rules
- ✅ Restrict who can push to matching branches
- ✅ Allow force pushes: **No**
- ✅ Allow deletions: **No**

## Best Practices

1. **Keep SEED Stable:** Only merge tested, reviewed code into SEED
2. **Small, Focused PRs:** Create pull requests that focus on a single feature or fix
3. **Regular Updates:** Regularly pull changes from SEED to keep your branch up-to-date
4. **Descriptive Names:** Use clear, descriptive names for your branches
5. **Clean History:** Consider squashing commits before merging to keep history clean
6. **Delete After Merge:** Delete feature branches after they're merged to reduce clutter

## Why SEED?

The name "SEED" represents:
- **S**table
- **E**ssential
- **E**volutionary
- **D**evelopment

It's the seed from which all development grows, making it a more meaningful name than generic terms like "main" or "master".

## Quick Reference

| Action | Command |
|--------|---------|
| Create feature branch | `git checkout -b feature/name` |
| Switch to SEED | `git checkout SEED` |
| Update SEED | `git pull origin SEED` |
| Push branch | `git push origin branch-name` |
| Delete local branch | `git branch -d branch-name` |
| Delete remote branch | `git push origin --delete branch-name` |
| View all branches | `git branch -a` |
| View branch status | `git status` |

## Contributing

All contributions should follow this branching strategy. For more details on contributing, see CONTRIBUTING.md (if available) or contact the repository maintainers.

---

Last Updated: December 2024  
Repository: Software-Stack-2025-Coding-S-lang-Needed-for-General-Coders-WINDOWS
