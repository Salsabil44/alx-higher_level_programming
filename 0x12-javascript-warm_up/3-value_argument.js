#!/usr/bin/node
// prints the first argument passed to it by sally 

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
