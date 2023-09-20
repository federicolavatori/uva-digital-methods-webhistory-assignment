# Digital Methods - Web History Assignment 

## Data Preparation

Following what is described [here](https://www.soothsawyer.com/how-to-take-full-page-screenshot-from-list-of-urls/) we performed the following steps:

1. Download Node JS and install it: https://nodejs.org/en/download/
2. Install Puppeteer by running this in your shell: npm i puppeteer
3. Download grab_url.js, grab_all.sh, and urls.txt and put them all in the same directory (or copy/paste the code further down this blog post)
4. Open a shell and change to the directory where you put the files from step 3.
5. Run: bash grab_all.sh 


## Data Analysis

We investigated how webpages changes across time by computing:
- Text similarity comparing extracted webpages as html
- Image similarity comparing captures screens as pngs

