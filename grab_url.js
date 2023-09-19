const puppeteer = require('puppeteer');
const args = process.argv.slice(2);
var index = args[0];
const url = args[1];
const filenameOption = args[2] || 'title'; // filenameOption will be 'title' if not specified

(async() => {
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--headless',
      '--disable-gpu'
    ]
  });

  console.log('index='+index+' url='+url);

  const page = await browser.newPage();
  await page.setDefaultNavigationTimeout(0);
  await page.setViewport({ width: 1024, height: 768 });

  try {
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 3000000 });
  } catch (error) {
    console.error(`Failed to load URL: ${url}, Error: ${error}`);
    await browser.close();
    process.exit(1);
  }

  page.on('console', (msg) => console.log('', msg.text()));

  await page.evaluate(`(${(async () => {

    const innerHeight = Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );
    console.log('height='+innerHeight+' ');

    await new Promise((resolve) => {
      let totalHeight = 0;
      let scrolled_times = 0;
      const distance = 100;

      const timer = setInterval(() => {
        const scrollHeight = innerHeight; //document.body.scrollHeight;
        scrolled_times++;
        window.scrollBy(0, distance);
        totalHeight += distance;
  
        if (totalHeight >= scrollHeight) {
            window.scrollTo(0, 0);
            console.log("scrolled "+scrolled_times+" times");
            clearInterval(timer);
            resolve();
        }
      }, 100);
    });
  })})()`);
 

  await page.waitForTimeout(1000);

  var filenameBase = filenameOption === 'url' ? url : await page.title();
  var filename = filenameBase.replace(/[^a-z0-9]/gmi, "_").replace(/\s+/g, "_");
  while (index.length < 4) {
    index = "0" + index;
  }

  // Ensure total filename length doesn't exceed 255 characters
  const MAX_FILENAME_LENGTH = 255;
  let reservedLength = index.length + 1 + 4; // 1 for "_" and 4 for ".png"
  if (reservedLength + filename.length > MAX_FILENAME_LENGTH) {
    filename = filename.substring(0, MAX_FILENAME_LENGTH - reservedLength);
  }

  filename = index + "_" + filename + '.png';

  console.log(`filename=${filename}\n`);

  try {
    await page.screenshot({
      path: filename,
      fullPage: true
    });
  } catch (error) {
    console.error(`Failed to take screenshot for URL: ${url}, Error: ${error}`);
    await browser.close();
    process.exit(1);
  } finally {
    await browser.close();
  }
})();