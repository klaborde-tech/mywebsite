# Keaton LaBorde Portfolio

A static portfolio for GitHub Pages. No build tools or installation needed.

## Preview

Open index.html in a modern browser. Keep style.css, app.js, and assets alongside it.

## Upload to the existing GitHub repository

1. Extract this ZIP.
2. Open the keaton-portfolio folder.
3. Upload its CONTENTS to the root of the mywebsite repository: index.html, style.css, app.js, assets, and .nojekyll. Do not upload the ZIP itself or place everything inside an extra keaton-portfolio folder.
4. Commit the files.
5. In repository Settings > Pages, select Deploy from a branch, choose the branch containing these files, and select / (root). Save.
6. Once deployment finishes, open https://klaborde-tech.github.io/mywebsite/ and refresh with Ctrl+Shift+R.

The existing index.html is replaced. Keep other existing files, especially the Projects directory: project downloads still link to those original files.

## Contents

- index.html: page content and nine projects
- style.css: responsive dark blue design and font declarations
- app.js: animated computational surface and motion control
- assets/: original photographs, logo, screenshots, and locally bundled fonts when available

Email, telephone, GitHub, LinkedIn, and project resource links remain functional. External resources require internet. The site does not require a backend.

## Changes from the single-file export

The font-import extraction in the earlier export stopped at a semicolon inside the font URL and corrupted the beginning of the CSS, including its custom property declarations. This package retains a complete, valid stylesheet. Relative paths work on GitHub Pages under /mywebsite/.
