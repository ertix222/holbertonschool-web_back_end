function createInt8TypedArray(length, position, value) {
  const Buffer = new ArrayBuffer(length);
  const view = new DataView(Buffer);

  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  view.setInt8(position, value);

  return Buffer;
}

export default createInt8TypedArray;
