# GitHub upload guide (browser method)

1. Sign in at https://github.com/.
2. Select **New repository**.
3. Repository name: `tu-wien-machine-learning-exercise-0`.
4. Description: `Reproducible dataset exploration for TU Wien Machine Learning Exercise 0 — Python analysis, data-quality checks and visualisations.`
5. Choose **Private** initially if you have not confirmed course/publication permissions and group consent. You can change visibility later.
6. Do not initialise with a README, .gitignore or licence because those files are already included in this package.
7. Create the repository.
8. Open the new repository and choose **Add file → Upload files**.
9. Open the extracted project folder on your computer and upload its contents, including the folders `data`, `plots`, `report`, and `scripts`, plus the root-level files. Keep the folder structure intact.
10. Do not upload your `.venv` folder or the original datasets unless redistribution is allowed. `.gitignore` helps exclude local data and environment files when using Git, but browser uploads can still upload files you manually select.
11. Enter commit message: `Add reproducible dataset exploration project`.
12. Select **Commit changes**.
13. Open the repository page and check that the README renders, images display, and the PDF opens.
14. Copy the repository URL and replace `[ADD YOUR REPOSITORY LINK]` in `LINKEDIN_POST.md` and the LinkedIn project entry.

## Important upload notes

- GitHub's browser upload supports files up to 25 MiB each and up to 100 files per upload batch. If a file is too large, use Git from the terminal or GitHub's recommended large-file workflow.
- The repository README explains the project and how to reproduce it. A person who clones/downloads the repository must still obtain the two original ARFF files separately and put them in `data/`.
- The GitHub repository is a public portfolio artefact only if you choose public visibility. Confirm the course rules and group members' consent first.
