#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const x of list) {
    if (x === searchElement) {
      count += 1;
    }
  }
  return count;
};
