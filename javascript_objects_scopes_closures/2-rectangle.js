#!/usr/bin/node
// 2-rectangle.js

class Rectangle {
  constructor(w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    // Otherwise, no properties are set → creates an empty object
  }
}

module.exports = Rectangle;
