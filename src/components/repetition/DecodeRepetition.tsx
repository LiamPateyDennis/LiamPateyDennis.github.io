
function EncodeRepetition(
  image: HTMLCanvasElement | ImageData | HTMLImageElement
): HTMLCanvasElement {
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
    } else {
      const imgEl = image as HTMLImageElement;
      srcCanvas.width = imgEl.naturalWidth || imgEl.width;
      srcCanvas.height = imgEl.naturalHeight || imgEl.height;
      ctx.drawImage(imgEl, 0, 0);
    }
  }

  const tileX = 3;
  const tileY = 1;
  const out = document.createElement("canvas");
  out.width = srcCanvas.width * tileX;
  out.height = srcCanvas.height * tileY;
  const outCtx = out.getContext("2d")!;

  for (let y = 0; y < tileY; y++) {
    for (let x = 0; x < tileX; x++) {
      outCtx.drawImage(srcCanvas, x * srcCanvas.width, y * srcCanvas.height);
    }
  }

  return out;
}

export default EncodeRepetition;
