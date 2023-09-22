# Digital Methods - Web History Assignment 

## Data Preparation

Following what is described [here](https://www.soothsawyer.com/how-to-take-full-page-screenshot-from-list-of-urls/) we performed the following steps:

1. Download Node JS and install it: https://nodejs.org/en/download/
2. Install Puppeteer by running this in your shell: npm i puppeteer
3. Download grab_url.js, grab_all.sh, and urls.txt and put them all in the same directory (or copy/paste the code further down this blog post)
4. Open a shell and change to the directory where you put the files from step 3.
5. Run: bash grab_all.sh 


## Data Analysis
Make sure you prepare a local environment in python with poetry to run this section. The analysis consists of two main activities:
- Resizing the pictures to have a uniform size across all the sample
- Investigated how webpages changes across time by computing similarity and dissimilarity measures as described [here](https://up42.com/blog/image-similarity-measures)