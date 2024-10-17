const { Builder, By, until } = require('selenium-webdriver');

describe('Login Page Tests', function () {
    let driver;

    before(async function () {
      this.timeout(20000); // Increase timeout to 10 seconds

        driver = await new Builder().forBrowser('chrome').build();
        await driver.get('http://localhost:3000/login'); // Update the URL to your app's login page
    });

    after(async function () {
        await driver.quit();
    });

    it('should login successfully', async function () {
        const { expect } = await import('chai');
        await driver.findElement(By.xpath('//*[@id="root"]/div/div/div/div[2]/a')).click();
        await driver.findElement(By.name('username')).sendKeys('root'); // Replace with your test username
        await driver.findElement(By.name('password')).sendKeys('1234'); // Replace with your test password
        await driver.findElement(By.xpath('//*[@id="root"]/div/div/div/div[2]/button')).click();
        
        // Add your assertions here, for example:
        await driver.wait(until.urlIs('http://localhost:3000/home'), 5000); // Replace with the expected URL after login
        const title = await driver.getTitle();
        expect(title).to.equal('Expected Title After Login'); // Replace with the expected title
    });
});
