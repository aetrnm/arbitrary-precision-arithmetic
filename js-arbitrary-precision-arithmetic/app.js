const BigNumber = require('./BigNumber.js').BigNumber;

function stringContainsNumber(string) {
  return string.match(/^[-+]?\d*$/) != null;
}

function createBigNumber(inputValue) {
  if (stringContainsNumber(inputValue)) {
    if (inputValue[0] === '-') {
      return new BigNumber(inputValue.slice(1), true);
    }
    return new BigNumber(inputValue);
  }
  throw new Error('Entered number is invalid!');
}

const fs = require('fs');
const fileRead = fs.readFileSync('INPUT.TXT', 'utf-8').split(/\r?\n/);
const inputValue1 = fileRead[0];
const inputValue2 = fileRead[1];

const number1 = createBigNumber(inputValue1);
const number2 = createBigNumber(inputValue2);
numberSum = new BigNumber();
numberSum._ = number1 + number2;
console.log(numberSum.toString());
