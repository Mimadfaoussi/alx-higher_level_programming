#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    return number.toString(parseInt(base));
  };
};
