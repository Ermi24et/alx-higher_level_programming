#!/usr/bin/node
exports.converter = function (base) {
  return (k) => k.toString(base);
};
