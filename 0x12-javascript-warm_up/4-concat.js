#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”

if (process.argv[2])
	console.log(process.argv[2] + " is ");
else
	console.log("undefined is ");
if (process.argv[3])
	console.log(argv[3]);
else
	console.log("undefined");