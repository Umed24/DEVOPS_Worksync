const { Builder, By, until } = require('selenium-webdriver');

describe('Signup Page Tests', function () {
    let driver;

    before(async function () {
      this.timeout(10000); // Increase timeout to 10 seconds

        driver = await new Builder().forBrowser('chrome').build();
        await driver.get('http://localhost:3000'); // Update the URL to your app's signup page
    });

    after(async function () {
        await driver.quit();
    });

    it('should Signup successfully', async function () {
        const { expect } = await import('chai');

        await driver.findElement(By.name('username')).sendKeys('newuser1122'); // Replace with your test username
        await driver.findElement(By.name('email')).sendKeys('new123@example1.com'); // Replace with your test email
        await driver.findElement(By.name('password')).sendKeys('your_password123'); // Replace with your test password
        await driver.findElement(By.xpath('//*[@id="root"]/div/div/div/div[2]/button')).click();
        await driver.wait(until.urlIs('http://localhost:3000/welcome'), 5000); // Replace with the expected URL after signup
        const title = await driver.getTitle();
        expect(title).to.equal('Expected Title After Signup'); // Replace with the expected title
    });
});
