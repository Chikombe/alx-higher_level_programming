#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let itr = 0;
  while ((len - itr) > 0) {
    const aux = list[len];
    list[len] = list[itr];
    list[itr] = aux;
    itr++;
    len--;
  }
  return list;
};
