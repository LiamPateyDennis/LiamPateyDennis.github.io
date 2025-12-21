// @param 2d binary array
// @returns HTMLCanvasElement - The input image to convert

function ConvertToImage(binaryArray: number[][]) {
  const height = binaryArray.length;
  const width = height > 0 ? binaryArray[0].length : 0;

  const out = document.createElement("canvas");
  out.width = width;
  out.height = height;
  const outCtx = out.getContext("2d")!;

  const imageData = outCtx.createImageData(width, height);
  const data = imageData.data;

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const v = binaryArray[y][x] === 1 ? 255 : 0;
      const idx = (y * width + x) * 4;
      data[idx] = v;
      data[idx + 1] = v;
      data[idx + 2] = v;
      data[idx + 3] = 255;
    }
  }

  outCtx.putImageData(imageData, 0, 0);
  return out;
}

export default ConvertToImage;
