#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let word;
    for (let i = 0; i < this.height; i++) {
      word = '';
      for (let j = 0; j < this.width; j++) {
        word = word + 'X';
      }
      console.log(word);
    }
  }
}
module.exports = Rectangle;
