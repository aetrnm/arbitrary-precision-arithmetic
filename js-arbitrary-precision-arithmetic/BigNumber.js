class BigNumber {
  maxNumberLength = 100;
  negativeness = false;

  constructor(value, negativeness = false) {
    if (arguments.length === 0) {
      value = 0;
    } else if (arguments.length > 2) {
      throw new Error('Need either 0, 1 or 2 arguments!');
    }
    this.value = value;
    this.negativeness = negativeness;
    this.arr = Array(maxNumberLength).fill(0);
    for (let i = value.length - 1; i >= 0; i--) {
      this.arr[i] = parseInt(this.value[value.length - i - 1]);
    }
  }

  valueOf() {
    BigNumber.operands.push(this);
    return 3;
  }

  add(first) {
    let carry = 0;
    this.arr = [...first.arr];
    [].slice.call(arguments, 1).forEach(function (second) {
      for (let i = 0; i < maxNumberLength; i++) {
        let that = this.arr[i] + second.arr[i] + carry;
        this.arr[i] = that % 10;
        carry = Math.floor(that / 10);
      }
    }, this);
    return this;
  }

  multiply(first) {
    //TODO
  }

  subtract(first) {
    //TODO
  }

  divide(first) {
    //NOT TODO
  }

  toString() {
    if (this.negativeness === false) {
      return this.arr.reverse().join('').replace(/^0+/, '');
    } else if (this.negativeness === true) {
      return '-' + this.arr.reverse().join('').replace(/^0+/, '');
    }
  }
  equals(other) {
    return JSON.stringify(this.arr) === JSON.stringify(other.arr);
  }
}

BigNumber.operands = [];

Object.defineProperty(BigNumber.prototype, '_', {
  set: function (value) {
    var ops = BigNumber.operands;
    var operator;
    if (ops.length === 2 && value === 0) {
      operator = this.subtract;
    } else if (ops.length === 2 && value === 1) {
      operator = this.divide;
    } else if (ops.length >= 2 && value === 3 * ops.length) {
      operator = this.add;
    } else if (ops.length >= 2 && value === Math.pow(3, ops.length)) {
      operator = this.multiply;
    } else {
      throw new Error('Unsupported operation (code ' + value + ')');
    }
    BigNumber.operands = [];
    return operator.apply(this, ops);
  },
  get: function () {
    return this.toString();
  },
});

exports.BigNumber = BigNumber;
