#!/usr/bin/node
function findSecondBiggest(args) {
  let max = -Infinity;
  let secondMax = -Infinity;

  args.forEach((val) => {
    const num = Number(val);
    if (num > max) {
      [secondMax, max] = [max, num];
    } else if (num < max && num > secondMax) {
      secondMax = num;
    }
  });

  return secondMax;
}

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  console.log(findSecondBiggest(args));
}
