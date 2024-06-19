#!/usr/bin/node
if (!process.argv[2] || isNaN(process.argv[2])) {
  console.log('Missing size');
} else if (parseInt(process.argv[2]) > 0) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let x = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      x = x + 'x';
    }
    console.log(x);
  }
}
