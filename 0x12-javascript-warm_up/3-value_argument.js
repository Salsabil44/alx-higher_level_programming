#!/usr/bin/node
//by sally
const arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
