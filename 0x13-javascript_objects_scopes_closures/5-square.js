#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.assign(this, {});
    }
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call Rectangle's constructor with the same size for width and height
    this.shapeName = 'Square';
  }
}

module.exports = Square;
