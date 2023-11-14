#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurences = 0;
  for (let itr = 0; itr < list.length; itr++) {
    if (searchElement === list[itr]) {
      nOccurences++;
    }
  }
  return nOccurences;
};
