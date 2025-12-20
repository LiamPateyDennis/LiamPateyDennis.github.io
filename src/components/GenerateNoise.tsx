function GenerateNoise(
  image: HTMLCanvasElement | ImageData | HTMLImageElement | null,
  noise: number
) {
  let srcCanvas: HTMLCanvasElement;

  if (image instanceof HTMLCanvasElement) {
    srcCanvas = image;
  } else {
    srcCanvas = document.createElement("canvas");
    const ctx = srcCanvas.getContext("2d")!;

    if ((image as ImageData).data && (image as ImageData).width) {
      const imgData = image as ImageData;
      srcCanvas.width = imgData.width;
      srcCanvas.height = imgData.height;
      ctx.putImageData(imgData, 0, 0);
    } else if (image === null) {
      throw new Error("No image provided to GenerateNoise");
    } else {
      const imgEl = image as HTMLImageElement;
      srcCanvas.width = imgEl.naturalWidth || imgEl.width;
      srcCanvas.height = imgEl.naturalHeight || imgEl.height;
      ctx.drawImage(imgEl, 0, 0);
    }
  }

  const out = document.createElement("canvas");
  out.width = srcCanvas.width;
  out.height = srcCanvas.height;
  const outCtx = out.getContext("2d")!;

  const imageData = outCtx.getImageData(0, 0, out.width, out.height);
  const data = imageData.data;

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
