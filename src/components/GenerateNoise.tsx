function GenerateNoise(image: HTMLCanvasElement | null, noise: number) {
  let srcCanvas: HTMLCanvasElement;

  if (image instanceof HTMLCanvasElement) {
    srcCanvas = image;
  } else {
    throw new Error("No image provided to GenerateNoise");
  }

  const out = document.createElement("canvas");
  out.width = srcCanvas.width;
  out.height = srcCanvas.height;
  const outCtx = out.getContext("2d")!;

  const imageData = outCtx.getImageData(0, 0, out.width, out.height);
  const data = imageData.data;

  console.log(out.width, out.height);
  console.log(data.length);

  // Generate Random Number of White Pixels
  for (let GenNum = 0; GenNum < noise * data.length; GenNum++) {
    let rngIndex: number = Math.floor(Math.random() * data.length);
    rngIndex = rngIndex - (rngIndex % 4); // align to pixel start
    data[rngIndex] = 255;
    data[rngIndex + 1] = 255;
    data[rngIndex + 2] = 255;
    data[rngIndex + 3] = 255;
    // preserve alpha channel (data[rngIndex+3])
  }
  outCtx.putImageData(imageData, 0, 0);
  return out;
}

export default GenerateNoise;
