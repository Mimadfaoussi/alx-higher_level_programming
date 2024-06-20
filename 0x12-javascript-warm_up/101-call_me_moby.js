#!/usr/bin/node

exports.callMeMoby = function (x, fun) {
  let i = 0;
  while (i < x) {
    fun();
    i++;
  }
};
